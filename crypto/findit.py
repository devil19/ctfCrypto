#!/usr/bin/env python
# -*- coding: utf-8 -*-


s1 = ['T', 'h', 'i', 's', 'I', 's', 'T', 'h', 'e', 'F', 'l', 'a', 'g', 'H', 'o', 'm', 'e']
s2 = ['p', 'v', 'k', 'q', '{', 'm', '1', '6', '4', '6', '7', '5', '2', '6', '2', '0', '3', '3', 'l', '4', 'm', '4', '9', 'l', 'n', 'p', '7', 'p', '9', 'm', 'n', 'k', '2', '8', 'k', '7', '5', '}']


input = s2
output=[]
re= ""

for i in range(38):
    ascii_value = ord(input[i])

    if  ascii_value >= 65 and ascii_value <= 90:

        ascii_value += 16
        if (ascii_value <= 90 or ascii_value>= 97) and ascii_value <122:
            continue
        ascii_value -= 26

    if ascii_value >97 :
        if ascii_value >122:
            continue
        ascii_value += 16
        if (ascii_value <= 90 or ascii_value>= 97) and ascii_value <122:
            continue
        ascii_value -= 26
    else:
        pass

    output.append(chr(ascii_value))

print re.join(output)