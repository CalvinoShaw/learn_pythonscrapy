from urllib.request import urlopen
from bs4 import BeautifulSoup


def getByAttr(url, tag, attributes):
	html = urlopen(url)
	bsObj = BeautifulSoup(html,"html.parser")
	nameList = bsObj.findAll(tag, attributes)
	for name in nameList:
		print(name.attrs["href"])


# getByAttr(
# 	"http://pythonscraping.com/pages/warandpeace.html",
# 	"span",
# 	{"class":"green"}
# 	)

getByAttr(
	"http://dangshi.people.com.cn/GB/234123/359282/index.html",
	"a",
	{"target":"blank"}
	)