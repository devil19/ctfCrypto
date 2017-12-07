#!/usr/bin/env python
# -*- coding: utf-8 -*-
import libnum
import gmpy2

f = open('res/rabinCrackflag.enc','r')
c = f.read()
c = libnum.s2n(c)
# p跟q通过题目给的公钥pem文件分解出来
p = 275127860351348928173285174381581152299
q = 319576316814478949870590164193048041239

n = p*q
r = pow(c,(p+1)/4,p)
s = pow(c,(q+1)/4,q)
a = gmpy2.invert(p,q)
b = gmpy2.invert(q,p)
x =(a*p*s+b*q*r)%n
y =(a*p*s-b*q*r)%n
print libnum.n2s(x%n)
print libnum.n2s((-x)%n)
print libnum.n2s(y%n)
print libnum.n2s((-y)%n)