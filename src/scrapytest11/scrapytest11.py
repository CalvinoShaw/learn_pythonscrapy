# 存储所有内容

from urllib.request import urlopen
from bs4 import BeautifulSoup,Comment
import re
import time
import requests
import csv

session = requests.Session()
headers = {
	"User-Agent":"Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
pages = set()
def getLinksAndTitle(pageNum):
	global pages
	url = "http://www.ccdi.gov.cn/fgk/law_display_" + str(pageNum)
	req = session.get(url, headers=headers)
	bsObj = BeautifulSoup(req.text,"html.parser")
	try:
		# 获取标题
		title = ' '.join((bsObj.find("div",{"class","flater_tab"}).find("h2").get_text()).split())

		# 获取页面注释，通过正则截取 文本来源 和 时间（注释）
		comments = ' '.join(bsObj.findAll(text=lambda text:isinstance(text, Comment)))
		sources = re.findall(r'(?<=来源：).+?(?=\</)',comments)
		source = str(sources)
		source = source.replace("['","")
		source = source.replace(" ']","")

		time1s = re.findall(r'(?<=时间：).+?(?=\</)',comments)
		time1 = str(time1s)
		time1 = time1.replace("['","")
		time1 = time1.replace(" ']","")

		# 获取文本内容
		contents = ' '.join((bsObj.find("div",{"class","flater_tab"}).find("div",{"class","TRS_Editor"}).get_text()).split())
		c = re.compile(r'(?<=TRS_Editor).+?(?=\})')
		content = c.sub(' ',contents)
		content = content.replace('TRS_Editor }',' ')
		content = content.replace('.',' ')
		content = content.replace(' ','')

		# 从文本中获取 时间（文本）
		time2 = ' '.join(re.findall(r"\d{4}年\d{0,2}月\d{0,2}日",content))
		t = re.compile(r'年|月|日')
		time2 = re.sub(t,'-',time2)

		return [title,source,time1,time2,content]

	except AttributeError as e:
		print (e)
		print(str(pageNum) + "出错了～")

def getAndSavaAsCSV():
	csvFile = open("./files/test.csv","w+")
	try:
		writer = csv.writer(csvFile)
		writer.writerow(("标题","来源","时间（注释）","时间（文本）"))
		# 6315-6319 没有相应页面
		# 6320 、6321、6322 、6330 、6331 正常
		# 6332及以后的页面基本不存在，但也可能存在正常页面
		for pageNum in range(1,7000):
			print (pageNum)
			backtitle = getLinksAndTitle(pageNum)
			if backtitle is None:
				continue
			writer.writerow((backtitle[0],backtitle[1],backtitle[2],backtitle[3]))
			time.sleep(4)
	except Exception as e:
		raise e
	finally:
		csvFile.close()

getAndSavaAsCSV()