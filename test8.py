#!/usr/bin/python
#coding:utf8

#局部变量和全局变量
#global 强制申明为全局变量
#函数若不调用。函数中申明的全局变量则无效

def fun():
    global a
    a = 200
    print a

fun()
print "#"*30
print a
