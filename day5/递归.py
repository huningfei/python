##算年龄
# def age(n):
#     if n == 3:
#         return 40
#     else:
#         return age(n+1)+2
# print(age(3))
##递归二分查找算法
l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# def cal(l,num,start,end):
#     if start<end:
#         mid = (end-start)//2 +start ##mid代表索引
#         print(start,end)
#
#         if l[mid]< num:
#             cal(l,num,mid+1,end)
#         elif l[mid]> num:
#             cal(l,num,start,mid-1)
#         else:
#             print('找到了',mid,l[mid])
#     else:
#         print('没找到')
# cal(l,58,0,len(l)-1)

def cal(l,num,start,end):
    '''

    :param l: 是列表
    :param num: 要找的数字
    :param start: 开始索引
    :param end: 结束索引
    :return:
    '''
    if start<end:
        mid = (end-start)//2 +start ##mid代表索引
        # print(start,end)

        if l[mid]< num:
            return  cal(l,num,mid+1,end)
        elif l[mid]> num:
            return cal(l,num,start,mid-1)
        else:
            return mid,l[mid]
    else:
        return '没找到'
print(cal(l,53,0,len(l)-1))
#l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]

# def cal(l,num,start=0,end=None):
#     # if end is None:end = len(l)-1
#     end = len(l)-1 if end is None else end
#     if start <= end:
#         mid = (end - start)//2 + start
#         if l[mid] > num :
#             return cal(l, num, start, mid-1)
#         elif l[mid] < num:      # 13  24
#             return cal(l,num,mid+1,end)
#         else:
#             return mid
#     else:
#         return None
# l = [2,3,5,10,15,16,18,22,26,30,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
# print(cal(l,56))



# print(len(l))