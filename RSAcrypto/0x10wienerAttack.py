#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 特征：
# n很大，并且e也很大

from rsa_wiener_attack.RSAwienerHacker import hack_RSA
from Crypto.PublicKey import RSA
from libnum import n2s


# 这里注意一个细节问题，如果在运行脚本的时候报错，请在脚本前加上：
# import   sys
# sys.setrecursionlimit(10000000)

A = RSA.importKey(open('res/wienerAttack.pub').read())
print "n = " + str(A.n)
print "len(n) = " + str(len(bin(A.n)) - 2)
print "e = " + str(A.e)

d = hack_RSA(A.e,A.n)
print d

# c为已知密文
c=0x1e04304936215de8e21965cfca9c245b1a8f38339875d36779c0f123c475bc24d5eef50e7d9ff5830e80c62e8083ec55f27456c80b0ab26546b9aeb8af30e82b650690a2ed7ea407dcd094ab9c9d3d25a93b2140dcebae1814610302896e67f3ae37d108cd029fae6362ea7ac1168974c1a747ec9173799e1107e7a56d783660418ebdf6898d7037cea25867093216c2c702ef3eef71f694a6063f5f0f1179c8a2afe9898ae8dec5bb393cdffa3a52a297cd96d1ea602309ecf47cd009829b44ed3100cf6194510c53c25ca7435f60ce5f4f614cdd2c63756093b848a70aade002d6bc8f316c9e5503f32d39a56193d1d92b697b48f5aa43417631846824b5e86

m = pow(c, d, A.n)
# 转成字符串
print n2s(m)