menu = {
    '北京': {
        '海淀': {
            '五道口': {
                'soho': {},
                '网易': {},
                'google': {}
            },
            '中关村': {
                '爱奇艺': {},
                '汽车之家': {},
                'youku': {},
            },
            '上地': {
                '百度': {},
            },
        },
        '昌平': {
            '沙河': {
                '老男孩': {},
                '北航': {},
            },
            '天通苑': {},
            '回龙观': {},
        },
        '朝阳': {},
        '东城': {},
    },
    '上海': {
        '闵行': {
            "人民广场": {
                '炸鸡店': {}
            }
        },
        '闸北': {
            '火车战': {
                '携程': {}
            }
        },
        '浦东': {},
    },
    '山东': {},
}
##堆栈
# l = [menu]
#
# # print(l[-1])
# while l:
#     for key in l[-1]:print(key)
#     k = input('input>>').strip()
#     if k in l[-1].keys() and l[-1] [k]:l.append((l[-1][k]))
#
#     elif k == 'b':l.pop()
#     elif k == 'q':break

##递归
# def func(dic):
#     while 1:
#         for key in dic:
#             print(key)
#         key = input('input>>').strip()
#         if key in dic.keys() and dic[key]:
#             ret = func(dic[key])
#             #print(ret)
#             if ret =='q':break
#         elif key =='b' or key == 'q':
#             #print(key)
#             return key
# func(menu)


def threeLM(dic):
    while True:
        for k in dic:print(k)
        key = input('input>>').strip()
        if key == 'b':return
        if key == 'q':return 'q'
        elif key in dic.keys() and dic[key]:
            ret = threeLM(dic[key])
            if ret == 'q': return 'q'

threeLM(menu)

