#!/usr/bin/python

a = int(raw_input("please input a:"))
b = int(raw_input("please input b:"))

def add(a,b):
    c = a+b
    d = a-b
    e = a*b
    f = a/b
    print "a+b:",c
    print "a-b:",d
    print "a*b:",e
    print "a/b:",f

add(a,b)

