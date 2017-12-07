# -*- conding: utf-8 -*-

import string

data = "70479679275221115227470416418414022368270835483295235263072905459788476483295235459788476"
strs = string.digits+string.lowercase

plaintext=""

for d in data:
    print int(d.strip())
    for a in strs:
        if ord(a)**19 % 920139713 == int(d.strip()):
            plaintext+=a
print plaintext