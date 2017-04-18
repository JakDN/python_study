#!/usr/bin/env python
# -*-coding:utf-8-*-

import getpass
# 引入模块getpass用于把输入的密码变成密文

_username = "jak"
_password = "333"
username = raw_input("username:")
password = getpass.getpass("password:")

# print username,password
# 条件判断，记住以:结尾
if username == _username and password == _password:
    print ("Welcome user {name} login...".format(name = username)) 
else:
    print ("Invalid username or password!")
