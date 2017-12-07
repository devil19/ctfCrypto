#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Crypto.PublicKey import RSA

A = RSA.importKey(open('res/readPempubkey.pem').read())
print A.n
print A.e
