#!/usr/bin/env python
# -*-coding:utf-8-*-

age_of_man = 33

# for循坏

for i in range(5):
    guess_age = int(raw_input("guess age:"))
    if guess_age == age_of_man:
        print ("you get it")
        break
    elif guess_age > age_of_man:
        print ("please guess smaller...")
    else:
        print ("guess bigger!")        
else:
    print ("you have try too more times...")


# for循环，设置步长
'''
for i in range(1,10,2):
    print i
'''
