#!/usr/bin/env python
# coding=utf-8

def hello(fn):
     def wrapper(*args,**kwargs):
        print "hello, %s" % fn.__name__
  
        user = {'name':'lzp','age':18,'email':'lzp@126.com'}
        return fn(user,*args,**kwargs)    #一次只能返回一个参数，此处返回字典参数
     return wrapper
  
@hello
def foo(test,a):  #可以同时接受其他形式的参数，但接受装饰器的参数必须在前面 
    print "my name is son parages %s" % a
    print "i am %s,my email is %s" % (test['name'],test['email'])  #打印字典的返回值，结果：i am lzp,my email is lzp@126.com
  
#foo()
foo("fuck")
  
"""
#test 是接收装饰器的传参,a 是往函数传参
 
hello, foo
my name is son parages fuck
i am lzp,my email is lzp@126.com
"""


##flask装饰器可以写成:
def login_required(f):
    """登陆装饰器"""
    @wraps(f)
    def wrapper(*args, **kwargs):
	user_name, user_role = get_request_user()
	if user_name:
    ┊   ┊   return f(*args, **kwargs)
    ┊   return redirect(url_for("user.login"))
    return wrapper
            
def admin_required(f):
    """需要管理员权限"""
    @wraps(f)
    def wrapper(*args, **kwargs):
    ┊   user_name, user_role = get_request_user()
    ┊   if user_name and user_role == 9:
    ┊   ┊   return f(*args, **kwargs)
    ┊   if user_name and user_role:
    ┊   ┊   return abort(403)
    ┊   return redirect(url_for("user.login"))
    return wrapper


再调用的时候直接装饰器修饰e
def get_request_user():
    user_name = getattr(g, 'user_name', None)
    user_role = None
    if not user_name:
    ┊   if 'user_name' in session:
    ┊   ┊   g.user_id = session['user_id']
    ┊   ┊   g.read_name = session['user_readname']
    ┊   ┊   user_name = session['user_name']
    ┊   ┊   user_role = session['user_role']
    ┊   g.user_name = user_name
    ┊   g.user_role = user_role
    return user_name, user_role

