#!/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import json
import requests

headers = {'content-type': 'application/json'}
url = "http://127.0.0.1:2000/api"
data = {
        'jsonrpc':'2.0',
        'method': 'idc.create',
        'id':'1',
    'params':{
        "name": "xiaoluo"
    }
}


r = requests.post(url, headers=headers,json=data)
print r.status_code
print r.text

