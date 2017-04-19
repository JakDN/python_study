#!/usr/bin/env python
# -*-coding:utf-8-*-

age_of_man = 43

# guess_age = int(raw_input("guess age:"))
# 循坏执行
'''
if guess_age == age_of_man:
    print ("yes you get it!")
elif guess_age > age_of_man:
    print ("think smaller...")
else:
    print ("think bigger!")
'''
count = 0
while count < 5:
    guess_age = int(raw_input("guess age:"))
    if guess_age == age_of_man:
        print ("yes you get it")
        break
    elif guess_age < age_of_man:
        print ("think bigger...")
    else:
        print ("think smaller!")
    count += 1
else:
    print ("you try too more times")
