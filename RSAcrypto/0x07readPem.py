#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA
from libnum import s2n
A = RSA.importKey(open('/Users/loo/Documents/CTF/crypto/rsa/hardRSA/pubkey.pem').read())
print A.n
print "n的长度：" + str(len(bin(A.n)) - 2)
print A.e
