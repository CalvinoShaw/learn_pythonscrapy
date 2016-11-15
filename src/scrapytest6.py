from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html,"html.parser")

	try:
		print("标题是："+bsObj.h1.get_text())
		print("段落内容是："+bsObj.find(id="mw-content-text").findAll("p")[0].get_text())
		print("页面编辑链接："+bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
	except AttributeError:
		print("页面缺少一些属性！")

	targets = bsObj.findAll("a",href=re.compile("^(/wiki/)"))
	for link in targets:
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print("--------------\n" + newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks("")