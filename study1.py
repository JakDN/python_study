#!/usr/bin/env python
#-*-coding:utf-8-*-
print "hello world"


# 定义字符串用单引号或者双引号，注释和多行字符串用三引号
# name = "jak"
msg = '''today
is 
a 
good
day
'''
'''
print name
print msg
'''

# 用户输入
# 用raw_input让用户输入，3.0以上用input
# input默认接收一个变量
name = raw_input("name:")
age = raw_input("age:")
print type(age)
# 默认输入为字符串

job = raw_input("job:")
salary = raw_input("salary:")

# 格式化输出
# %s表示字符串占位
# %()用来传参数

info = '''
-------------info of %s----------------
Name:%s
Age:%s
Job:%s
Salary:%s
'''%(name,name,age,job,salary)

# 用format定义参数
info2 = '''
--------------info of {_name}--------------
Name:{_name}
Age:{_age}
Job:{_job}
Salary:{_salary}
'''.format(_name = name,
           _age = age,
           _job = job,
           _salary = salary)

# 用format传参数，{数字}来代替参数定义，需要注意数字的顺序
info3 = '''
----------info of {0}------------
Name:{0}
Age:{1}
Job:{2}
Salary:{3}
'''.format(name,age,job,salary)

print info3

