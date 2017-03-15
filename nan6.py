#!/usr/bin/python

a = int(raw_input("a:"))
b = int(raw_input("b:"))
def compare(a,b):
    if a>b:
        print "a is big"
    if a==b:
        print "a is as big as b"
    if a<b:
        print "b is bigger"

compare(a,b)

