#!/usr/bin/env python
import time


d = {1:111,2:222,3:333,4:444,5:555}
for x in range(20):
    print x
    time.sleep(2)
    if x == 1:
        pass
    if x == 2:
        print "helle world"
        continue
    if x == 10:
        break
    if x == 6:
        exit()
    print "I am ok!"
else:
    print "hi"

for x in range(10):
    print "-------------->",x
