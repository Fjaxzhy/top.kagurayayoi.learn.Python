#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python支持七种运算符

#   变量定义:
a = 10
b = 20
List = [1, 2, 3, 4, 5]

# 算术运算符
result = a + b  # 相加
print(result)
result = a - b  # 减去
print(result)
result = a * b  # 相乘
print(result)
result = b / a  # 除去
print(result)
result = b % a  # 取模
print(result)
result = a ** b  # b次幂   返回a的b次幂
print(result)
result = a // b  # 取整除  向下取接近商的整数
print(result)

# 比较运算符
if a == b:      # 等于
    print(True)
if a != b:      # 不等于
    print(True)
if a > b:       # 大于
    print(True)
if a < b:       # 小于
    print(True)
if a >= b:      # 大于等于
    print(True)
if a <= b:      # 小于等于
    print(True)

# 赋值运算符
c = 10      # 直接赋值
print(c)
c += a      # 加法赋值 等效 c = c + a
print(c)
c -= a      # 减法赋值 等效 c = c - a
print(c)
c *= a      # 乘法赋值 等效 c = c * a
print(c)
c /= a      # 除法赋值 等效 c = c / a
print(c)
c %= a      # 取模赋值 等效 c = c % a
print(c)
c **= a     # 幂赋值   等效 c = c ** a
print(c)
c //= a     # 取整除赋值 等效 c = c // a
print(c)
# if (n := len(a)) > 10:  # 海象运算符  赋值表达式可以避免调用 len() 两次

# 逻辑运算符
if a and b:     # x and y 布尔'与'
    print(True)
if a or b:      # x or y  布尔'或’
    print(True)
if not (a and b):   # not x 布尔'非'
    print(True)

# 位运算符
d = 60  # bin: 0011 1100
e = 13  # bin: 0000 1101
print(d & e)    # 按位与   12 / 0000 1100
print(d | e)    # 按位或   61 / 0011 1101
print(d ^ e)    # 按位异或  49 / 0011 0001
print(~d)       # 按位取反  -61 / 1100 0011
print(d << 2)   # 左移    240 / 1111 0000
print(d >> 2)   # 右移    15 / 0000 1111

# 成员运算符
if a in List:       # 如果在指定的序列中找到值返回 True 否则返回 False
    print(True)
if a not in List:   # 如果在指定的序列中没有找到值返回 True 否则返回 False
    print(True)

# 身份运算符
if a is b:      # 判断两个标识符是不是引用自一个对象
    print(True)
if a is not b:  # 判断两个标识符是不是引用自不同对象
    print(True)
