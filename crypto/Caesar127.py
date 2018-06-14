
import base64

lstr='''T?^i\?fB^ArfO*DqS-f=L@@OMePHPA^/NfLIK*/OTtDMPOP.JN*'''

for p in range(127):
    str1 = ''
    for i in lstr:
        temp = chr((ord(i)+p)%127)
        if 32<ord(temp)<127 :
            str1 = str1 + temp
            feel = 1
        else:
            feel = 0
            break
    if feel == 1:
        print(str1)


print base64.b64decode('''dGhlIGtleSBpcyBDQTJEMTgyNTNCNTg2RUEx==''')
