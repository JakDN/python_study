#!/usr/bin/python

def f(name='nan',age=29):
    print "name:%s" %name
    print "age:%s" %age

d = {"name":"chennan","age":30}
f(**d)
