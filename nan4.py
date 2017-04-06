#!/usr/bin/python

x = ""
while x != "q":
    print "hello nan"
    x = raw_input("please input somthing q to quit:")
    if  not x :
        break
    if x == "c":
        continue
    print "one time again"
else:
    print "ending.........."    
