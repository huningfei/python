import os
import shutil
import traceback
import paramiko

from io import StringIO
import subprocess
from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from django.conf import settings
from web.forms.deploy import DeployModelForm, DeployPushForm
from web import models
from web.utils.pager import Pagination
from web.utils.urls import memory_reverse


def deploy_list(request, project_id):
    """
    部署任务列表
    :param request:
    :param project_id:
    :return:
    """
    page = request.GET.get('page', 1)
    # 数据库中数据总条数
    total_count = models.Deploy.objects.filter(project_id=project_id).count()
    # 数据库中获取即可
    pager = Pagination(page, total_count, request.path_info)
    depart_queryset = models.Deploy.objects.filter(project_id=project_id)[pager.start:pager.end]

    project = models.Project.objects.filter(id=project_id).first()

    return render(request, 'deploy_list.html', {'depart_queryset': depart_queryset, 'pager': pager, 'project': project})


def deploy_rollback_list(request, project_id):
    '''
    回滚项目
    :param request:
    :param project_id:
    :return:
    '''
    deploy_object_all = models.Deploy.objects.all()  # 所有任务

    deploy_object = models.Deploy.objects.filter(project_id=project_id).first()

    if request.method == 'GET':
        # 1. 显示发布信息
        # 2. 用户选择主机

        all_host_list = deploy_object.project.hosts.all()  # 显示所有关联这个项目的主机

        deployed_host_list = models.DeployRecord.objects.filter(deploy=deploy_object)  # 这个项目里已经发布的主机
        all_project_version = deployed_host_list.values_list("host__deployrecord__host_version")
        # a=models.DeployRecord.objects.filter(host=all_host_list).all().values_list('host_version')
        # print(a)

        # print(host_version)

        # host_version=models.DeployRecord.objects.filter(host_version=deployed_host_list)

        # print(all_project_version)

        deployed_host_dict = {item.host_id: item for item in deployed_host_list}  # 主机id：主机名
        # form = DeployPushForm(deploy_object.project)
        return render(request, 'deploy_rollback_list.html',
                      {'deploy_object': deploy_object, 'all_host_list': all_host_list,
                       'deployed_host_dict': deployed_host_dict, 'deploy_object_all': deploy_object_all})

    host_id_list = request.POST.getlist('hosts')  # 前端页面给选中的主机的id
    host_list = models.Host.objects.filter(id__in=host_id_list)


def deploy_add(request, project_id):
    """
    添加任务
    :param request:
    :param project_id:
    :return:
    """
    if request.method == 'GET':
        form = DeployModelForm()
        return render(request, 'form.html', {'form': form})
    form = DeployModelForm(data=request.POST)
    # 对用户提交的数据进行校验
    if form.is_valid():
        form.instance.project_id = project_id
        form.save()
        return redirect(memory_reverse(request, 'deploy_list', project_id=project_id))
    return render(request, 'form.html', {'form': form})


def deploy_edit(request, project_id, nid):
    """
    编辑
    :param request:
    :param nid: 当前要编辑的项目id
    :return:
    """
    obj = models.Deploy.objects.filter(id=nid).first()  # 包含此行的所有数据
    if request.method == "GET":
        # 生成HTML标签 + 携带默认值
        form = DeployModelForm(instance=obj)
        return render(request, 'form.html', {'form': form})  # 带默认值
    form = DeployModelForm(data=request.POST, instance=obj)
    if form.is_valid():
        form.instance.project_id = project_id
        form.save()
        return redirect(memory_reverse(request, 'deploy_list', project_id=project_id))
    return render(request, 'form.html', {'form': form})


def deploy_del(request, project_id, nid):
    """
    删除
    :param request:
    :param nid:
    :return:
    """
    origin = memory_reverse(request, 'deploy_list', project_id=project_id)
    if request.method == 'GET':
        return render(request, 'delete.html', {'cancel': origin})
    models.Deploy.objects.filter(id=nid).delete()
    return redirect(origin)


def deploy_fetch(request, project_id, deploy_id):
    """
     点击上线按钮执行的代码
    :param request:
    :param project_id: 项目id
    :param deploy_id: 部署id
    :return:
    """
    # print(request.user.git_name)
    # print(request.user.git_pwd)
    # 部署的是那个项目
    deploy_object = models.Deploy.objects.filter(id=deploy_id, project_id=project_id).first()
    # 下载代码所在路径   deploy_object.project.title 项目名   deploy_object.version项目版本
    cwd_path = os.path.join(settings.BASE_DIR, 'codes', deploy_object.project.title, deploy_object.version)

    # print(cwd_path)

    # 1. 获取代码  仓库地址 + 版本 + subprocess
    def get_code():
        # 判断代码存放路径是否存在,遇到的问题是删除不了目录
        project_path = os.path.join(cwd_path, deploy_object.project.title)
        if os.path.exists(project_path):  # 如果存在就删除，不然不能下载代码
            shutil.rmtree(project_path)

        # 判断仓库是否私有
        if deploy_object.project.private:
            protcal, addr = deploy_object.project.git.split("//", maxsplit=1)
            git_addr = "%s//%s:%s@%s" % (protcal, request.user.git_name, request.user.git_pwd, addr)

        else:
            git_addr = deploy_object.project.git

        # 克隆仓库到本地，-b指定版本
        # cmd = "git clone -b %s %s" % (deploy_object.version, git_addr)
        cmd = "git clone  %s" % (git_addr)
        if not os.path.exists(cwd_path):  # 如果存放代码的目录不存在，就创建
            os.makedirs(cwd_path)
        subprocess.check_call(cmd, shell=True, cwd=cwd_path)

    get_code()

    # 2. 编译代码
    def compile_code():
        pass

    compile_code()

    # 3.打包文件
    def package_code():
        import shutil
        import time
        ctime = time.strftime('%Y%m%d%H%M%S')  # 时间戳
        project_code_path = os.path.join(cwd_path, deploy_object.project.title)  # 项目所在路径
        print(project_code_path)

        file_name = "%s%s" % (deploy_object.project.title, ctime)  # 文件名字
        zip_file_path = os.path.join(cwd_path, file_name)  # 压缩之后文件的名字
        shutil.make_archive(base_name=zip_file_path, format='zip', root_dir=project_code_path)  # 压缩成zip格式
        return file_name + '.zip'

    zip_file_name = package_code()
    deploy_object.uid = zip_file_name  # 上线文件包名称
    deploy_object.status = 2
    deploy_object.save()
    response = {
        'code': True,
        'status': deploy_object.get_status_display(),  # 显示status_choice类型的中文名字
        'uid': zip_file_name  # 文件名

    }
    return JsonResponse(response)
    # return redirect(memory_reverse(request, 'deploy_list', project_id=project_id))


def deploy_push(request, project_id, deploy_id):
    """
    推送代码,发布按钮执行的代码
    :param request:
    :param project_id:
    :param deploy_id:
    :return:
    """
    deploy_object = models.Deploy.objects.filter(id=deploy_id, project_id=project_id).first()
    if request.method == 'GET':
        # 1. 显示发布信息
        # 2. 用户选择主机
        # 通过deploy跨project表，然后在跨到hosts表，去查询主机
        all_host_list = deploy_object.project.hosts.all()  # 显示所有关联这个项目的主机
        deployed_host_list = models.DeployRecord.objects.filter(deploy=deploy_object)  # 这个项目里已经发布过的主机
        deployed_host_dict = {item.host_id: item for item in deployed_host_list}  # 主机id：主机名
        # form = DeployPushForm(deploy_object.project)
        return render(request, 'deploy_push.html',
                      {'deploy_object': deploy_object, 'all_host_list': all_host_list,
                       'deployed_host_dict': deployed_host_dict})

    host_id_list = request.POST.getlist('hosts')  # 获取前端页面给选中的主机的id hosts是前端name的值
    host_list = models.Host.objects.filter(id__in=host_id_list)

    from concurrent.futures import ThreadPoolExecutor
    def task(host_object, deploy_object):
        cwd_path = os.path.join(settings.BASE_DIR, 'codes', deploy_object.project.title,
                                deploy_object.version)  # 存放路径

        # 1. 在DeployRecord中创建一条发布任务
        def create_deploy_record():
            record_object = models.DeployRecord.objects.get_or_create(deploy=deploy_object, host=host_object,
                                                                      host_version=deploy_object.version)
            return record_object

        record_object, is_new = create_deploy_record()  # 调用这个函数

        # 2 推送
        def push_code():
            status=False
            try:

                private_key = paramiko.RSAKey(file_obj=StringIO(request.user.server_private_key))  # 获取用户私钥

                transport = paramiko.Transport((host_object.hostname, host_object.ssh_port))  # 主机名和端口号
                transport.connect(username=request.user.server_name, pkey=private_key)  # 用户名和私钥
                # 用户远程上传下载文件
                sftp = paramiko.SFTPClient.from_transport(transport)
                # 远程执行命令
                ssh = paramiko.SSHClient()
                ssh._transport = transport
                # 创建目录
                code_file_path = os.path.join(cwd_path, deploy_object.uid) # 存放代码的目录
                target_folder_path = '/home/yx/codes/%s/%s/' % (
                    deploy_object.project.title, deploy_object.version)
                stdin, stdout, stderr = ssh.exec_command('mkdir -p %s' % target_folder_path)
                stdout.read()
                # 上传代码到服务器
                target_file_path = os.path.join(target_folder_path, deploy_object.uid)  # 文件存放目录
                sftp.put(code_file_path, target_file_path)
                transport.close()
            except Exception as e:
                return status

        status = push_code()

        # if not status:  # 如果没有就返回空，不往下执行了
        #     return
        def publish():
            """
            上传脚本
            执行脚本
            :return:
            """
            private_key = paramiko.RSAKey(file_obj=StringIO(request.user.server_private_key))  # 获取用户私钥
            transport = paramiko.Transport((host_object.hostname, host_object.ssh_port))  # 主机名和端口号
            transport.connect(username=request.user.server_name, pkey=private_key)  # 用户名和私钥
            # 用户远程上传下载文件
            sftp = paramiko.SFTPClient.from_transport(transport)
            # 远程执行命令
            ssh = paramiko.SSHClient()
            ssh._transport = transport
            # 创建脚本目录
            code_file_path = os.path.join(cwd_path, deploy_object.uid)
            target_folder_path = '/home/yx/script/%s/%s/' % (
                deploy_object.project.title, deploy_object.version)  # /home/yx/script/dbhot/v4.0
            stdin, stdout, stderr = ssh.exec_command('mkdir -p %s' % target_folder_path)
            stdout.read()
            # 上传数据库里面的脚本内容到服务器

            script_file_name = deploy_object.uid.split('.')[
                                   0] + "." + deploy_object.script.interpreter  # 脚本名字，项目名字+时间戳+.py
            #
            target_file_path = os.path.join(target_folder_path, script_file_name)  # /home/yx/script/dbhot/v4.0 +脚本名字
            file_object = sftp.open(target_file_path, mode='w')  # 在指定目录下打开一个文件，然后写入
            file_object.write(deploy_object.script.code)  # 把数据库里面的脚本内容拿到

            # # 执行脚本
            command = 'python3 %s %s %s %s' % (
                target_file_path, deploy_object.project.title, deploy_object.version, deploy_object.uid)
            # python3 /home/yx/script/dbhot/v4.0/dbhot20181228104300.py dbhot v4.0 dbhot20181228104300.zip
            print(command)

            stdin, stdout, stderr = ssh.exec_command(command)
            result = stdout.read()
            file_object.close()  # 关闭刚才的写文件
            transport.close()
            return target_file_path

        publish()

        # 发布成功之后，更新主机状态

        record_object.status = 2
        record_object.save()

    #
    # pool = ThreadPoolExecutor(30)
    # for obj in host_list:
    #     # pool.submit(task, obj, deploy_object)
    #     pool.submit(task,obj,deploy_object)
    # pool.shutdown()
    for host in host_list:
        task(host, deploy_object)
    return redirect(memory_reverse(request, 'deploy_push', project_id=project_id, deploy_id=deploy_id))
