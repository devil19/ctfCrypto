#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string


# 所有可打印字符
print string.printable

# 3233转为二进制
print bin(3233)
# 3233的二进制长度
print len(bin(3233)) - 2


# 3233转为十六进制
print hex(3233)
# 3233的十六进制长度
print len(hex(3233)) - 2

# 二进制转十进制
print int('0b110010100001', 2)
print int('110010100001', 2)

# 整形 转 ASCII
print chr(102)

# ASCII 转 整形
print ord('f')


