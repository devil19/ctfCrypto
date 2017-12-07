#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64

str = ""
l=[89,51,82,109,89,50,86,122,97,71,107,61]
for i in l:
    str= str+chr(i)

print base64.b64decode(str)

