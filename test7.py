#!/usr/bin/python
#coding:utf8

def machine(a,b="巧克力"):
    print "这是一个",a,"元",b,"口味的雪糕！"

x = raw_input("input price:")
y = raw_input("input tast:")

machine(x,y)


#参数的默认值必须从右往左定义
#这是一个注释
