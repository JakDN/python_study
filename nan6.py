#!/usr/bin/python

x = int(raw_input("a:"))
y = int(raw_input("b:"))
def compare(a,b):
    if a>b:
        print "a is big"
    if a==b:
        print "a is as big as b"
    if a<b:
        print "b is bigger"

compare(x,y)

