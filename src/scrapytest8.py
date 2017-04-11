# 开始使用 requests 避开 403 forbidden

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import requests

session = requests.Session()
headers = {
	"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}
pages = set()

def getLinks(pageNum):
	global pages
	url = "http://www.ccdi.gov.cn/fgk/law_display_" + str(pageNum)
	req = session.get(url, headers=headers)
	bsObj = BeautifulSoup(req.text)
	try:
		print(str(pageNum) + " 标题是："+' '.join((bsObj.find("div",{"class","flater_tab"}).find("h2").get_text()).split()))
	except AttributeError:
		print(str(pageNum) + " 页面缺少一些属性！")

for pageNum in range(1,6000):
	getLinks(pageNum)
	time.sleep(3)
