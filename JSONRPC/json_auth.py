#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys

from flask import Flask
 

from flask_jsonrpc import JSONRPC

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

def check_auth(username, password):
    if username=="xiaoluo" and password == "123":
        return True
    else:
	return False
   

@jsonrpc.method('App.index', authenticated=check_auth)
def index():
    return u'Welcome to Flask JSON-RPC'

@jsonrpc.method('App.echo(name=str) -> str', validate=True, authenticated=check_auth)
def echo(name='Flask JSON-RPC'):
    return u'Hello {0}'.format(name)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)


###########json测试：

#!/usr/bin/env python
from flask_jsonrpc.proxy import ServiceProxy
proxy = ServiceProxy('http://127.0.0.1:5000/api')
print proxy.App.index('xiaoluo', '123')
##{u'jsonrpc': u'2.0', u'id': u'1e80bc94-494f-4b0b-9e22-9b30fb0c0d56', u'result': u'Welcome to Flask JSON-RPC'}
print proxy.App.index()
##{u'jsonrpc': u'2.0', u'id': u'335c84d8-61e8-409a-bbec-201942d3599b', u'error': {u'executable': u'/usr/bin/python', u'code': -32602, u'name': u'InvalidParamsError', u'message': u'InvalidParamsError: Authenticated methods require at least [username, password] 
print proxy.App.echo(username='xiaoluo', password='123', name='Flask')
##{u'jsonrpc': u'2.0', u'id': u'4f04fe80-24ec-47dd-af79-aaab979a6863', u'result': u'Hello Flask'}

