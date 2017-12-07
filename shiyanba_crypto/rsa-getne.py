 #!/usr/bin/env python
# -*- coding: utf-8 -*-
# 从pem文件提取公钥

from Crypto.PublicKey import RSA
pub = RSA.importKey(open(u'/Users/loo/Desktop/安全培训/0802/1501571698_59802a72ab8d3/pub.pem').read())
n = long(pub.n)
e = long(pub.e)
print n
print e