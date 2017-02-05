# -*- coding: utf-8 -*- 

import re
import os

def deletePunctuation(filename):
	f1 = open("source/"+filename,'r+')
	oldcontent = f1.read()
	oldcontent = oldcontent.decode("utf8")
	oldcontent = ' '.join(oldcontent.split())
	newcontent = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！：，。？?、；~@#￥%……&*《》（）]+".decode("utf8"), "".decode("utf8"),oldcontent)
	print(newcontent)
	f1.close()
	writenewcontent(filename,newcontent)


def writenewcontent(filename,newcontent):
	f2 = open("newsource/"+filename,'w+')
	f2.write(newcontent.encode("utf-8"))
	f2.close()


def getFileList():
	newfilelist = []
	oldfilelist = os.listdir(os.getcwd()+"/source")
	for oldfile in oldfilelist:
		newfilename = oldfile.decode('utf-8').encode('utf-8')
		# print(newfilename)
		newfilelist.append(newfilename)
	for item in newfilelist[1:28]:
		print("-----------")
		print(item)
		print("-----------")
		deletePunctuation(item)

	# print(newfilelist[0])
		# deletePunctuation(newfilename.decode("utf-8").encode("utf-8"))


def aboutcoding():
	import sys
	print(sys.getdefaultencoding())
	reload(sys)
	sys.setdefaultencoding("utf-8")
	print(sys.getdefaultencoding())

def main():
	filename = "违规发放津贴补贴行为处分规定副本.txt".decode("utf-8").encode("utf-8")
	deletePunctuation(filename)


getFileList()