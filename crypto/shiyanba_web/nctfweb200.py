#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys,base64
from string import maketrans
def rot13(data):
    intable = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    outtable = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    table = maketrans(intable,outtable)
    return data.translate(table)
if __name__ == '__main__':
    data = "a1zLbgQsCESEIqRLwuQAyMwLyq2L5VwBxqGA3RQAyumZ0tmMvSGM2ZwB4tws"
    data = rot13(data)
    data = data[::-1]
    data = base64.b64decode(data)
    result=''
    for i in data:
        result += chr(ord(i)-1)
    result = result[::-1]
    print result