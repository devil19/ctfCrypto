#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 有一个zip文件，但是不知道完整的密码，但知道解压密码一部分的sha1值
# 不完整的密码 "*7*5-*4*3?" *代表可打印字符
# 不完整的sha1值 "619c20c*a4de755*9be9a8b*b7cbfa5*e8b4365*"
#
#    用python 爆破
#

import string
import hashlib
import re


def work():
    zidian = string.printable;
    pattern  = re.compile(r'619c20c.a4de755.9be9a8b.b7cbfa5.e8b4365.')
    count = 0
    print "zidian长度：" + str(len(zidian))
    for i in zidian:
        for j in zidian:
            count += 1
            print str(count)
            for n in zidian:
                for m in zidian:
                    tmp = i + "7" + j + "5" + "-" + m + "4" + n + "3?"
                    sha1_value = hashlib.sha1(tmp).hexdigest()
                    if re.match(pattern=pattern, string=sha1_value):
                        return tmp
print work()


