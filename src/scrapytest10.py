# 采集包括内容、来源、时间在内的 文本

from urllib.request import urlopen
from bs4 import BeautifulSoup,Comment
import re
import time
import requests

session = requests.Session()
headers = {
	"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
pages = set()
def getLinksAndTitle(pageNum):
	global pages
	url = "http://www.ccdi.gov.cn/fgk/law_display_" + str(pageNum)
	req = session.get(url, headers=headers)
	bsObj = BeautifulSoup(req.text,"html.parser")
	try:
		print (str(pageNum))
		title = ' '.join((bsObj.find("div",{"class","flater_tab"}).find("h2").get_text()).split())
		print (title)
		getSourceAndTime1(bsObj)
		getContentAndTime2(bsObj)
	except AttributeError as e:
		print (e)
		print(str(pageNum) + "出错了～")

def getSourceAndTime1(bsObj):
	# 获取页面注释，通过正则截取 文本来源 和 时间（注释）
	comments = ' '.join(bsObj.findAll(text=lambda text:isinstance(text, Comment)))
	source = re.findall(r'(?<=来源：).+?(?=\</)',comments)
	time1 = re.findall(r'(?<=时间：).+?(?=\</)',comments)
	
	# 打印输出
	print (source)
	print (time1)

def getContentAndTime2(bsObj):
	# 获取文本内容
	contents = ' '.join((bsObj.find("div",{"class","flater_tab"}).find("div",{"class","TRS_Editor"}).get_text()).split())
	c = re.compile(r'(?<=TRS_Editor).+?(?=\})')
	content = c.sub(' ',contents)
	content = content.replace('TRS_Editor }',' ')
	content = content.replace('.',' ')
	content = content.replace(' ','')

	# 从文本中获取 时间（文本）
	time2 = ' '.join(re.findall(r"\d{4}年\d{0,2}月\d{0,2}日",content))
	
	# 打印输出
	print (time2)
	print (content)

def printResults():
	for pageNum in range(1,2):
		getLinksAndTitle(pageNum)	
		print ("-----------------------------")
		# time.sleep(3)

printResults()
