# txt文本去除标点

import string
import re
punct = string.punctuation

f1 = open('test.txt','r')
f2 = open('testwrite.txt','r+')
for line in f1.readlines():
	newline = re.sub("[\s+\.\!\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*《》（）]+", "", line)
	print(newline)
	f2.write(newline)
f1.close()
f2.close()