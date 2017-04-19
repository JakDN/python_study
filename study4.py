#! /usr/bin/env python
# -*-coding:utf-8-*-


age_of_man = 24

count = 0

while count < 3:
    guess_age = int(raw_input("guess age:"))
    if guess_age == age_of_man:
        print ("you get it!")
        break
    elif guess_age > age_of_man:
        print ("think smaller...")
    else:
        print ("think bigger!")
    count += 1
    if count == 3:
        countine_confirm = raw_input("do you want to keep guessing?")
        if countine_confirm != "n":
            count = 0
#else:
#    print ("you have try too more times...")
  
