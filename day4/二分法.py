##使用二分法的前提是列表必须是从小到大排序的
# l=[1,3,34,56,76,87,98,123]
# def search(l,number):
#     print(l)
#     if len(l) ==0:
#         print('number not exist')
#         return
#     num_index=len(l) // 2
#     if number > l[num_index]:
#         #往右找
#         search(l[num_index+1:],number)
#     elif number < l[num_index]:
#         #往左找
#         search(l[0:num_index],number)
#     else:
#         print('find it')
# search(l,234)

def cal(l,num,start=0,end=None):
    