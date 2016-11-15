from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://dangshi.people.com.cn/GB/234123/359282/index.html")
bsObj = BeautifulSoup(html,"html.parser")
targets = bsObj.findAll("a",{"target":"blank"})
for link in targets:
	if 'href' in link.attrs:
		print(link.attrs['href'])