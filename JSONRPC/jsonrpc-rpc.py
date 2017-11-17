#!/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

headers = {'content-type': 'application/json'}
url = "http://127.0.0.1:9000/api"
data = {
	'jsonrpc':'2.0',
	'method': 'user.list',
	'id':'1'

}


r = requests.post(url, headers=headers,json=data)
print r.status_code
print r.text




