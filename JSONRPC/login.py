#!/usr/bin/env python
#coding:utf-8
from flask import Flask,render_template,request
from flask_jsonrpc import JSONRPC
import json

app = Flask(__name__)
jsonrpc = JSONRPC(app, '/api')

@jsonrpc.method('user.list')
def index(username, passwd):
    if username=='chen' and passwd=='123':
        return 'Hello,Flask JSON-RPC Blueprint...Correct!'
    else:
        return 'Hello,Flask JSON-RPC Blueprint...Fail!'

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8000,debug=True)
