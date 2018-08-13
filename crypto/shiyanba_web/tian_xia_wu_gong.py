#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import base64



value = base64.b64decode(requests.get('http://ctf5.shiyanbar.com/web/10/10.php').headers['FLAG']).split(':')[1]
print requests.post('http://ctf5.shiyanbar.com/web/10/10.php',data={'key':value}).content

#print requests.post('http://ctf4.shiyanbar.com/web/10.php',data={'key':base64.b64decode(requests.get('http://ctf4.shiyanbar.com/web/10.php').headers['FLAG']).split(':')[1]}).content