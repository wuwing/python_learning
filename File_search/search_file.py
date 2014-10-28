#-*-coding:utf-8-*-
'''指定当前目录之下的后缀名为pdf的全部文件的搜索'''
''' v1.0 版本 
	希望能够自己输入目录
	文件类型依然是以pdf为结尾'''

import os,os.path
import re
global flag
flag = False
def print_pdf(root,dirs,files):
	global flag
	for file in files:
		path = os.path.join(root,file)
		"""得到文件的完整路径"""
		path = os.path.normcase(path)
		'''规范路径的大小写'''
		if re.search(r".*\.pdf",path):
			print path
			flag = True

road = raw_input("Enter the original directory:\n")#手动输入初始路径
while not os.path.exists(road):#非法路径
	road = raw_input("No such directory,please enter the directory again:\n")

for root,dirs,files in os.walk(road):
	print_pdf(root,dirs,files)

if flag == False:
	print "No such file"
#没有找到该文件
