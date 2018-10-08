# n=0
# while n<=100:
#     n=n+1
#     num=n%2
#     if num==0:
#         print(n)
#

with open("cy_ip_list",encoding="utf-8",mode='r') as f1, open("error_list",encoding="utf-8",mode='r') as f2:
    count = 0
    for i in f2:
        i = i.strip()
        # print(i)
        for ip in f1:
            ip=ip.strip()
            # print(ip)
            # if count == 0:
            #     print(count)
            #     # pass
            #     print(ip.strip())

            if i in ip:

                print(ip.strip())
                f1.seek(0)
                break
            count += 1
