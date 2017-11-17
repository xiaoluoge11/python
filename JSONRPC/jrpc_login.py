from flask_jsonrpc.proxy import ServiceProxy
result=ServiceProxy('http://127.0.0.1:8000/api').user.list(username='chen', passswd='123')
print result
