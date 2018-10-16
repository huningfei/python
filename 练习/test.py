import os
# path = 'file'
path=r'D:\file'
print('正在读写文件，请稍等......')
for filename in os.listdir(path):
    fullname = os.path.join(path, filename)
    # print(fullname)

    # f = open(fullname, 'rb')
    # f_read = f.read().decode('gbk')
    # # print(f_read)
    # f.close()
    #
    # f2 = open('full.xls', encoding='gbk', mode='a+')
    #
    # f2.write(f_read)
    # f2.close()

    # 如果是linux系统导出来的数据用utf-8,如果是windows则用gbk
    f1 = open(fullname, encoding='utf-8')

    try:
        for i in f1:
            if "电子邮箱" in i:
                continue
            with open('test.xls',encoding='gbk',mode='a+')as f2:
                f2.write(i)
                f2.close()
        f1.close()
    except Exception:
        print(fullname)





