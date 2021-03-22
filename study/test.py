"""
测试字符串基本语法
"""

# word = '字符串'
# str = "这是一个句子。"
# paragraph = """这是一个段落，
# 可以由多行组成"""
#
#
# print(str)  # 输出字符串
# print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
# print(str[0])  # 输出字符串第一个字符
# print(str[2:5])  # 输出从第三个开始到第五个的字符
# print(str[2:])  # 输出从第三个开始后的所有字符
# print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
# print(str * 2)  # 输出字符串两次
# print(str + '你好')  # 连接字符串
#
# print('------------------------------')
#
# print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
# print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义
#
# input("\n\n按下 enter 键后退出。")

# import sys
#
# x = 'runoob'
# sys.stdout.write(x + '\n')

# expression = 1
# if expression:
#     print('if')
# elif expression:
#     print('elif')
# else:
#     print('else')

# x = "a"
# y = "b"
# # 换行输出
# print(x)
# print(y)
#
# print('---------')
# # 不换行输出
# print(x, end=",")
# print(y, end=" ")
# print()

# import sys
# print('================Python import mode==========================')
# print ('命令行参数为:')
# for i in sys.argv:
#     print (i)
# print ('\n python 路径为',sys.path)

from sys import argv, path  # 导入特定的成员

# print('================python from import===================================')
# print('argv:', argv)  # 因为已经导入path成员，所以此处引用时不需要加sys.path
# print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

# Fibonacci series: 斐波纳契数列
# 两个元素的总和确定了下一个数
# a, b = 0, 1
# while b < 10:
#     print(b)
#     a, b = b, a + b

# i = 256 * 256
# print('The value of i is : ', i)

# a, b = 0, 1
# while b < 1000:
#     print(b,end=',')
#     a, b = b, a + b


# age = int(input("请输入你家狗狗的年龄: "))
# print("")
# if age < 0:
# 	print("请输入正确的年龄。")
# elif age == 1:
# 	print("相当于 14 岁的人。")
# elif age == 2:
# 	print("相当于 22 岁的人。")
# elif age > 2:
# 	human = 22 + (age -2)*5
# 	print("对应人类年龄: ", human)
# ### 退出提示
# input('点击 enter 键退出')

# print(1 // 3 )
# a = ['him', 25, 100, 'her']
# print(a)
#
# a = (1991, 2014, 'physics', 'math')
# print(a,type(a), len(a))

#
# student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
# print('Tom' in student)
#
# dic = {}  # 创建空字典
# tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
# print(tel)
# print(tel['Jack'])
# del tel['Rose']
# tel['Mary'] = 4127  # 添加一个键值对
#
# print(list(tel.keys()))
# print(sorted(tel.keys()))
# print("tom" in tel)
# print('god' not in tel)


# test=dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
# print(test)
# test={x: x**2 for x in (2, 4, 6)}
# print(test)
# test=dict(sape=4139, guido=4127, jack=4098)
# print(test)

# word="cesdfdgfhg"
# print(word[7])


# import sys
#
# def fibonacci(n): # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
#
# while True:
#     try:
#         print (next(f), end=" ")
#     except StopIteration:
#         sys.exit()


# n = 100
#
# sum = 0
# counter = 1
# while counter <= n:sum = sum + counter;counter += 1;print("Sum of 1 until %d: %d" % (n,sum))

# languages = ["C", "C++", "Perl", "Python"]
# for x in languages:
#     print (x)

# edibles = ["ham", "spam","eggs","nuts"]
# for food in edibles:
#     if food == "spam":
#         print("No more spam please!")
#         break
#     print("Great, delicious " + food)
# else:
#     print("I am so glad: No spam!")
# print("Finally, I finished stuffing myself")

# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i, a[i])


# import sys
#
# print('命令行参数如下:')
# for i in sys.argv:
#    print(i)
#
# print('\n\nPython 路径为：', sys.path, '\n')
#
# print(dir())


# for x in range(1, 11):
#     print(str(x).rjust(2), str(x * x).rjust(3), end=' ')
#     # 注意前一行 'end' 的使用
#     print(str(x * x * x).rjust(4))
#
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))

# 使用pickle模块将数据对象保存到文件

# import pickle
#
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
#
# selfref_list = [1, 2, 3]
#
# selfref_list.append(selfref_list)
#
# output = open('test.txt', 'w')
#
# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)
#
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
# #
# output.close()


# 使用pickle模块从文件中重构python对象

# import pprint, pickle
#
# pkl_file = open('data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()


# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again   ")
#     print("测试")

# def divide(x, y):
#     try:
#         result = x / y
#     except ZeroDivisionError:
#         print("division by zero!")
#     else:
#         print("result is", result)
#     finally:
#         print("executing finally clause")
#
# divide(2,1)
# divide(2,0)
# divide('2','1')

# with open("data.txt") as f:
#     for line in f:
#         print(line, end="")

# import re
#
# x=re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest gffgg')
# print(x)

# from urllib.request import urlopen
#
# for line in urlopen('https://www.baidu.com/'):
#     line = line.decode('utf-8')  # Decoding the binary data to text.
#     # if 'EST' in line or 'EDT' in line:  # look for Eastern Time
#     print(line)


# from datetime import date
#
# now = date.today()
# print(now)
#
# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# print(now)
#
# birthday = date(1964, 7, 31)
# print(birthday)
# age = now - birthday
# print(age)
# print(age.days)


# 写文件
# with open("test.txt", "wt") as out_file:
#     out_file.write("该文本会写入到文件中\n看到我了吧！")
#
# # Read a file
# with open("test.txt", "rt") as in_file:
#     text = in_file.read()
#
# print(text)


# import re
#
# line = "Cats are smarter than dogs";
#
# matchObj = re.match( r'dogs', line, re.M|re.I)
# if matchObj:
#    print ("match --> matchObj.group() : ", matchObj.group())
# else:
#    print ("No match!!")
#
# matchObj = re.search( r'dogs', line, re.M|re.I)
# if matchObj:
#    print ("search --> matchObj.group() : ", matchObj.group(0))
# else:
#    print ("No match!!")


# import pymysql
#
# # 打开数据库连接
# db = pymysql.connect(host="localhost", user="root", password="123456", database="ag_admin", charset="utf8")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print ("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()


# import _thread
# import time
#
# # 为线程定义一个函数
# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
#
# # 创建两个线程
# try:
#    _thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    _thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print ("Error: 无法启动线程")
#



# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
#     def __init__(self, threadID, name, counter):
#         threading.Thread.__init__(self)
#         self.threadID = threadID
#         self.name = name
#         self.counter = counter
#     def run(self):
#         print ("开始线程：" + self.name)
#         print_time(self.name, self.counter, 5)
#         print ("退出线程：" + self.name)
#
# def print_time(threadName, delay, counter):
#     while counter:
#         if exitFlag:
#             threadName.exit()
#         time.sleep(delay)
#         print ("%s: %s" % (threadName, time.ctime(time.time())))
#         counter -= 1
#
# # 创建新线程
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # 开启新线程
# thread1.start()
# thread2.start()
# thread1.join()
# thread2.join()
# print ("退出主线程")

# import json
#
# # Python 字典类型转换为 JSON 对象
# data = {
#     'no' : 1,
#     'name' : 'W3CSchool',
#     'url' : 'http://www.w3cschool.cn'
# }
#
# json_str = json.dumps(data)
# print ("Python 原始数据：", repr(data))
# print ("JSON 对象：", json_str)
#
#
# # 将 JSON 对象转换为 Python 字典
# data2 = json.loads(json_str)
# print ("data2['name']: ", data2['name'])
# print ("data2['url']: ", data2['url'])
#
# # 写入 JSON 数据
# with open('data.json', 'w') as f:
#     json.dump(data, f)
#
# # 读取数据
# with open('data.json', 'r') as f:
#     data = json.load(f)

import time

localtime = time.localtime(time.time())
print ("本地时间为 :", localtime)

localtime = time.asctime( time.localtime(time.time()) )
print ("本地时间为 :", localtime)

# 格式化成2020-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# 格式化成Sat Mar 28 22:24:24 2020形式
print(time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()))

# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2020"
print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))


import calendar
cal = calendar.month(2020, 9)
print ("以下输出2020年9月份的日历:")
print (cal)