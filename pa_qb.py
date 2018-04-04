#coding:utf-8
#python2
#爬虫糗百，实现保存到本地txt
import re
from urllib import request

url = 'https://www.qiushibaike.com/text/'
req = request.Request(url)
header1 = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
header2 = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:50.0) Gecko/20100101 Firefox/50.0'
req.add_header('User-Agent',header1)
with request.urlopen(req) as f:
    data = f.read()
    print('status: ',f.status, f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    data = data.decode('utf-8')
    print(data)
    pattern = re.compile(u'content">\s*<span>\s*(\s.*?\s)\s*</span>.*?(\d+)</i>.*?(\d+)</i>',re.S)
    items = re.findall(pattern,data)
    print('n=: ',len(items))
    fp = open('qb.txt','wb')
    for each in items:
        if int(each[1])>1000:
#            fp.write(each[1].encode())
            fp.write(('\n\n'+each[1]+' like赞').encode())
            fp.write(each[0].encode())
    fp.close()
