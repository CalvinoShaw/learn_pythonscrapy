# -*- coding: utf-8 -*- 

import string
import re
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

def test():
	f1 = open("test.txt",'r+')
	content = f1.read().decode("gbk")
	print(content)
	utfcontent = u''.join((content)).encode('utf-8').strip()
	print(utfcontent)
	newcontent = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*《》（）]+", "", utfcontent)
	print(newcontent)

def deletePunctuation(oldfile):
	punct = string.punctuation
	f1 = open(os.getcwd()+"/source/"+oldfile,'r',encoding='utf-8')
	f2 = open("new_" + oldfile,'w+')
	for line in f1.readlines():
		newline = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*《》（）]+", "", line)
		print(newline)
		f2.write(newline)
	f1.close()
	f2.close()


def getFileList():

	oldfilelist = os.listdir(os.getcwd()+"/source")
	newfilelist = os.listdir(os.getcwd()+"/source")
	for oldfile in oldfilelist:
		deletePunctuation(oldfile)

def function():
	import re  
	temp = temp.decode("utf8")  
	string = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+".decode("utf8"), "".decode("utf8"),temp)  
	print string  
	# if (len(FileNames)>0):
	# 	for fn in FileNames:
	# 		if (len(FlagStr)>0):  
	# 			# 返回指定类型的文件名  
	# 			if (IsSubString(FlagStr,fn)):  
	# 				fullfilename=os.path.join(FindPath,fn)  
	# 				FileList.append(fullfilename)  
	# 		else:
	# 			# 默认直接返回所有文件名  
	# 			fullfilename=os.path.join(FindPath,fn)  
	# 			FileList.append(fullfilename)

	# 对文件名排序
	# if (len(FileList)>0):  
	# 	FileList.sort()  
  
	# return FileList
	# print (FileList)

test()