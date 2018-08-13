#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
import base64

def main(h_str):
    output = ''
    t = [16,32,48]
    for i in range(len(h_str)/2):
        output += chr(int(h_str[2*i:2*(i+1)],16)^t[i%3])
    return output

if __name__ == '__main__':
    uname1 = 'FlappyPig'
    code2 = '5D4F7A2552462153'
    code1 = main(uname1.encode('hex')).encode('hex').upper()
    uname2 = main(code2)
    m = hashlib.md5()
    m.update(code1+uname2)
    print 'code1:'+code1
    print 'uname2:'+uname2
    print 'flag:ctf{'+m.hexdigest()+'}'