#python3.x
#-*- encoding:utf-8 -*- 
decode_set=["utf-8",'gb18030', 'ISO-8859-2','gb2312',"gbk","Error" ]#编码集
#GBK不如GB18030覆盖得好，容易出错，故首先尝试GB18030。
for k in decode_set:#编码集循环
        try:
            directions = "原文/20 - 关于厉行节约反对食品浪费的意见.txt"
            file = open(directions,"r",encoding=k)
            #打开路径中的文本
            readfile = file.read()#这步如果解码失败就会引起错误，跳到except。
            print("open file %s with encoding %s" %(directions,k))#打印读取成功
            readfile = readfile.encode(encoding="utf-8",errors="replace")#若是混合编码则将不可编码的字符替换为"?"。
            break#打开路径成功跳出编码匹配
        except:
            if k=="Error":#如果碰到这个程序终止运行
                raise Exception("%s had no way to decode"%directions)
            continue
        print("done!")