#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 小指数攻击
# 条件：e特别小，比如e为3，N非常大
# 攻击方法：直接暴力搜索，对于给定的密文，每次加上N，直到可以开三次根为整数。

#from gmpy2 import iroot
import gmpy
from libnumSkill import n2s

n=22297438048747269084668540548451075863697230316653829979974766264037201288683962161805975218606091995006130774808955539752875140782316727212105999696527131465934655046004790537960872091980166123411315052309079498420607841421247264531922117703195318039364311581700525131351979022710906386748056454542460271638541382899446214550199566437929001010047362849553798762483138636321018729693026538570107613275416663305123403057997135200290324262461965489374460932097451640809963516688449930838072464936715548241448176034327352770246471027737140032671088236665050898710889588790999714069123042393091902555727321368525503937627
e=3
c=12175939426970015887948740543449508154181029340303424301244310710949983113367165043729908960135196986281877848102228614978027162537129618294649050515600098469644444691627004911075322400887079623827580886534946692562187346359967702178428117522833198160545314208985161727153343851325430875448562875530846585243017643194013848124024049551233109316312427973164515514862534965179016555315721921892573576456640646970607520597993273135258867140880318666123793239149053340882301883052248780427106001520573134454535340585245965555212208548409209115188408379247161949482960877243139275969531252402182851924756473191677978648702
k = 0
while True:
    # (x, y) = iroot(c+k*n, e)
    (m, y) = gmpy.root(c+k*n, e)
    if y == 1:
        print m
        break
    print "k= "+ str(k)
    k += 1
m = n2s(m)
print "明文：" + m