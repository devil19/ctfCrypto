#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rsa

with open('res/pubkey.txt','r') as f:
    pubkey = rsa.PublicKey.load_pkcs1(f.read().encode())

n = pubkey.n
print "n= ", n
print "e= ", pubkey.e