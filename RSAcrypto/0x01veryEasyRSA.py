#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 已知 p,q,e,c
# 求解 d,m

from libnum import n2s,s2n

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def get_c_from_enc():

    # 从文件中读取密文，并转换成十进制数
    f = open('res/veryEasyRSAflag.enc','rb')
    c= f.read()
    c = s2n(c)
    f.close()
    return c

# c = get_c_from_enc()
c = 49412914049026066227292604633959399022586841904231599586841156187258952420473
p = 319576316814478949870590164193048041239
q = 275127860351348928173285174381581152299
e = 65537
d = modinv(e, (p-1)*(q-1))
print d


# 利用pow函数求出明文的十进制表示 m=pow(c,d,n)
m = pow(c, d, p*q)
# 转成字符串
print n2s(m)
# print hex(m)
# print hex(m)[2:len(hex(m))-1].decode('hex')


