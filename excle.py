# # -*- coding: utf-8 -*-
#
# # 将多个Excel文件合并成一个
# import xlrd
# import xlsxwriter
#
#
# # 打开一个excel文件
# def open_xls(file):
#     fh = xlrd.open_workbook(file)
#     return fh
#
#
# # 获取excel中所有的sheet表
# def getsheet(fh):
#     return fh.sheets()
#
#
# # 获取sheet表的行数
# def getnrows(fh, sheet):
#     table = fh.sheets()[sheet]
#     return table.nrows
#
#
# # 读取文件内容并返回行内容
# def getFilect(file, shnum):
#     fh = open_xls(file)
#     table = fh.sheets()[shnum]
#     num = table.nrows
#     for row in range(num):
#         rdata = table.row_values(row)
#         datavalue.append(rdata)
#     return datavalue
#
#
# # 获取sheet表的个数
# def getshnum(fh):
#     x = 0
#     sh = getsheet(fh)
#     for sheet in sh:
#         x += 1
#     return x
#
#
# if __name__ == '__main__':
#     # 定义要合并的excel文件列表
#     allxls = ['D:/test/a.xls', 'D:/test/b.xls']
#     # 存储所有读取的结果
#     datavalue = []
#     for fl in allxls:
#         fh = open_xls(fl)
#         x = getshnum(fh)
#         for shnum in range(x):
#             print("正在读取文件：" + str(fl) + "的第" + str(shnum) + "个sheet表的内容...")
#             rvalue = getFilect(fl, shnum)
#     # 定义最终合并后生成的新文件
#     endfile = 'D:/test/excel3.xlsx'
#     wb1 = xlsxwriter.Workbook(endfile)
#     # 创建一个sheet工作对象
#     ws = wb1.add_worksheet()
#     for a in range(len(rvalue)):
#         for b in range(len(rvalue[a])):
#             c = rvalue[a][b]
#             ws.write(a, b, c)
#     wb1.close()
#     print("文件合并完成")
import glob  # 需要用pip先安装
from numpy import *  # 请提前在CMD下安装完毕，pip install numpy
import xlrd  # 同上
import xlwt  # 同上
import time

location = "D:/file/"  # 你需要合并该目录下excel文件的指定的文件夹
date = "20171016"  # 不需要，笔者在这里使用此参数作为合并后的excel文件名称
header = ["学校", "年级","班级","用户key","用户编号","用户姓名","电子邮箱","身份证号","生日","性别","绑定设备号"]  # 表头，请根据实际情况制定
fileList = []
for fileName in glob.glob(location + "*.xls"):
    fileList.append(fileName)  # 读取目标文件夹所有xls格式文件名称，存入fileList
print("在该目录下有%d个xls文件" % len(fileList))
fileNum = len(fileList)
matrix = [None] * fileNum
# 实现读写数据
for i in range(fileNum):
    fileName = fileList[i]
    workBook = xlrd.open_workbook(fileName)
    try:
        sheet = workBook.sheet_by_index(0)
    except Exception as e:
        print(e)
    nRows = sheet.nrows
    matrix[i] = [0] * (nRows - 1)
    nCols = sheet.ncols
    for m in range(nRows - 1):
        matrix[i][m] = ["0"] * nCols
    for j in range(1, nRows):
        for k in range(nCols):
            matrix[i][j - 1][k] = sheet.cell(j, k).value
fileName = xlwt.Workbook()
sheet = fileName.add_sheet("combine")
for i in range(len(header)):
    sheet.write(0, i, header[i])
rowIndex = 1
for fileIndex in range(fileNum):
    for j in range(len(matrix[fileIndex])):
        for colIndex in range(len(matrix[fileIndex][j])):
            sheet.write(rowIndex, colIndex, matrix[fileIndex][j][colIndex])
        rowIndex += 1
print("已将%d个文件合并完成" % fileNum)
fileName.save(location + date + ".xls")
# fileName.save("D:\python21\python\.txt")
