from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
	try:
		html = urlopen(url)
	except (HTTPError, URLError) as e:
		return None
	try:
		bsObj = BeautifulSoup(html.read())
		links = bsObj.a
	except AttributeError as e:
		raise None
	return links

links = getTitle("http://dangshi.people.com.cn/GB/234123/359282/index.html")
if links == None:
	print("Links could not be found")
else:
	print(links)