#-*-coding:utf-8-*-
'''指定当前目录之下的后缀名为pdf的全部文件的搜索'''
import os,os.path
import re

def print_pdf(root,dirs,files):
	for file in files:
		path = os.path.join(root,file)
		"""得到文件的完整路径"""
		path = os.path.normcase(path)
		'''规范路径的大小写'''
		if re.search(r".*\.pdf",path):
			print path

for root,dirs,files in os.walk('.'):
	print_pdf(root,dirs,files)
