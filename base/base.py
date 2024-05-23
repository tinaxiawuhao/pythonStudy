#不可变数据（3 个）：Number（数字）、String（字符串）、Tuple（元组）；
#可变数据（3 个）：List（列表）、Dictionary（字典）、Set（集合）。
# Numbers
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a),type(b),type(c),type(d))
print("==============================")
# String
"""
1、反斜杠可以用来转义，使用 r 可以让反斜杠不发生转义。
2、字符串可以用 + 运算符连接在一起，用 * 运算符重复。
3、Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始。
4、Python 中的字符串不能改变。
"""
s = "C:\some\name"
s2 = r"C:\some\name"
print(s, type(s), len(s))
print(s2, type(s), len(s))
print("==============================")
# Tuple
"""
1、与字符串一样，元组的元素不能修改。
2、元组也可以被索引和切片，方法都是一样的。
3、注意构造包含 0 或 1 个元素的元组的特殊语法规则。
4、元组也可以使用 + 操作符进行拼接。
"""
a = (1991, 2014, 'physics', 'math')
print(a, type(a), len(a))
#构造包含 0 个或 1 个元素的 tuple 是个特殊的问题，所以有一些额外的语法规则：
tup1 = () # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(tup1, type(tup1), len(tup1))
print(tup2, type(tup2), len(tup2))
print("==============================")
# List
"""
1、List 写在方括号之间，元素用逗号隔开。
2、和字符串一样，List 可以被索引和切片。
3、List 可以使用 + 操作符进行拼接。
4、List 中的元素是可以改变的。
"""
a = ['him', 25, 100, 'her']
print(a)
print("==============================")
# Set
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 重复的元素被自动去掉
'Rose' in student  # membership testing（成员测试）
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)     # a和b的差集
print(a | b)     # a和b的并集
print(a & b)     # a和b的交集
print(a ^ b)     # a和b中不同时存在的元素
print("==============================")
# Dictionaries
"""
1、字典是一种映射类型，它的元素是键值对。
2、字典的关键字必须为不可变类型，且不能重复。
3、创建空字典使用 { }
"""
dic = {}  # 创建空字典
tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(tel)
print(tel['Jack'])   # 主要的操作：通过key查询
del tel['Rose']  # 删除一个键值对
tel['Mary'] = 4127  # 添加一个键值对
print(tel)
print(list(tel.keys()))  # 返回所有key组成的list
print(sorted(tel.keys())) # 按key排序
print('Tom' in tel)       # 成员测试
print('Mary' not in tel)  # 成员测试
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(dict)
print({x: x**2 for x in (2, 4, 6)})
dict(sape=4139, guido=4127, jack=4098)
print(dict)