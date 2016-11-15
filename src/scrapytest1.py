from urllib.request import urlopen
from bs4 import BeautifulSoup
# html = urlopen('http://cpc.people.com.cn/xijinping/')
# html = urlopen('http://pythonscraping.com/pages/page1.html')
html = urlopen('http://dangshi.people.com.cn/GB/234123/359282/index.html')
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.a)