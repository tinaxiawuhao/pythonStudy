# -*- coding: UTF-8 -*-

# Python 程序用于检测用户输入的数字是否为质素

# 用户输入数字
num = int(input("请输入一个数字: "))

# 质素大于 1
if num > 1:
   # 查看因子
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"不是质素")
           print(i,"乘于",num//i,"是",num)
           break
   else:
       print(num,"是质素")
       
# 如果输入的数字小于或等于 1，不是质素
else:
   print(num,"不是质素")