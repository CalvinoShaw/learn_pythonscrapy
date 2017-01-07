# 开始使用 requests 避开 403 forbidden

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import time
import requests

# user_agents = [
#     'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
#     'Opera/9.25 (Windows NT 5.1; U; en)',
#     'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
#     'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
#     'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
#     'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
#     "Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7",
#     "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0 ",
# ]

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
		# s = 
		# result = ' '.join(s.split())
		print(str(pageNum) + " 标题是："+' '.join((bsObj.find("div",{"class","flater_tab"}).find("h2").get_text()).split()))
	except AttributeError:
		print(str(pageNum) + " 页面缺少一些属性！")




for pageNum in range(1,6000):
	getLinks(pageNum)
	time.sleep(3)

	# for link in targets:
	# 	if 'href' in link.attrs:
	# 		if link.attrs['href'] not in pages:
	# 			newPage = link.attrs['href']
	# 			print("--------------\n" + newPage)
	# 			pages.add(newPage)
	# 			getLinks(newPage)