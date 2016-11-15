from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
	global pages
	html = urlopen("http://en.wikipedia.org"+pageUrl)
	bsObj = BeautifulSoup(html,"html.parser")
	targets = bsObj.findAll("a",href=re.compile("^(/wiki/)"))
	for link in targets:
		if 'href' in link.attrs:
			if link.attrs['href'] not in pages:
				newPage = link.attrs['href']
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks("")