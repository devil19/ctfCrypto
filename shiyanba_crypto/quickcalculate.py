#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

value = requests.get("http://172.19.191.2/web1/").content.split('''math">''')[1].split('''</div>''')[0]
print value

result = eval(value)
print result

print requests.post("http://172.19.191.2/web1/",data={'res': value}).content.decode('gb2312')