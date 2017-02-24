import os

def getFileList():
	newfilelist = []
	oldfilelist = os.listdir(os.getcwd()+"/原文")
	for oldfile in oldfilelist:
		newfilename = oldfile
		# print(newfilename)
		newfilelist.append(newfilename)
	for item in newfilelist[1:76]:
		# print(item)
		doSearch(item)

def doSearch(filename):
	searchcontent = "八项规定"
	file = open("原文/"+filename,'r+',encoding="gb18030")
	filecontent = file.read()
	if searchcontent in filecontent:
		print (filename)
	else:
		print("false")

# doSearch()
getFileList()