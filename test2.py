#!/usr/bin/env python


d = {"name":"jak","age":29,"work":"IT"}
l = [1,2,4,6,7,9,"jak","ding"]
str = "hello"
for x in range(len(str)):
    print str[x]

for x in range(len(l)):
    if x >=5:
        print l[x]

for x in d:
    print d[x]

for k,v in d.items():
    print k,v



