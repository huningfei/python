# 1. agent形式在每个客户端上面运行
# import subprocess
# result = subprocess.getoutput("dir")
# print(result)


# 2. SSH模式必须用paramiko模块 ，在一个中控机上面运行，相当于跳板机

import paramiko
#用户名密码方式
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='58.132.0.208', port=8888, username='root', password='@@lanpa20180625')
stdin, stdout, stderr = ssh.exec_command('ifconfig')
result = stdout.read()
ssh.close()
print(result)


# 公钥私钥方式
# import paramiko
# private_key = paramiko.RSAKey.from_private_key_file('/home/auto/.ssh/id_rsa')
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname='c1.salt.com', port=22, username='wupeiqi', pkey=private_key)
# stdin, stdout, stderr = ssh.exec_command('df')
# result = stdout.read()
# ssh.close()

# 3. SaltStack模式 在saltstack主上面运行

# import subprocess
# subprocess.getoutput('salt "c1.com" cmd.run "命令"')