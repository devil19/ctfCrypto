#!/usr/bin/env python
# -*- coding: utf-8 -*-

str1="synt{ebg13fbrnfl}"
flag=""
for i in xrange(0,len(str1)):
    flag+=chr(ord(str1[i])^i)
print 'CTF{%s}'%flag