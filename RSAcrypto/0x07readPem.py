#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from libnum import s2n
A = RSA.importKey(open('res/readPempubkey.pem').read())
print "n = " + str(A.n)
print "len(n) = " + str(len(bin(A.n)) - 2)
print "e = " + str(A.e)
