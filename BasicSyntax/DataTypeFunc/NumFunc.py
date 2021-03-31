#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 基本数据类型-函数 数字类型
from math import *
from random import *

# 数字类型转换

x = '100'
print(int(x))  # 转换成整数
x = '50.5'
print(float(x))  # 转换成浮点数
x = '100'
print(complex(x))  # 转换为复数 实数为x 虚数为0
x = 50
y = 20
print(complex(x, y))  # 转换为复数 实数为x 虚数为y

# 数学函数
abs(-10)  # 返回绝对值
ceil(4.1)  # 返回数字的上入整数
exp(1)  # 返回e的x次幂(e^x)
fabs(-10)  # 同abs() 返回浮点数绝对值
floor(4.9)  # 返回数字的下舍整数
log(100, 10)  # 返回以y为基数的x的对数
log10(100)  # 返回以10为基数的x的对数
max([1, 2, 3, 4])  # 返回给定参数的最大值
min([1, 2, 3, 4])  # 返回给定参数的最小值
modf(50.5)  # 返回x的整数部分与小数部分
pow(10, 10)  # 返回x**y运算后的值
round(10.5, 0)  # 返回浮点数x地四舍五入值 n值代表舍入到小数点后的位数
sqrt(100)  # 返回x的平方根

# 随机数函数
seq = range(10)
choice(seq)  # 从序列中随机选出一个元素
randrange(0, 100, 1)  # 从指定范围内 按指定基数递增的集合中随机获取一个数 基数默认为1
random()  # 随机生成下一个实数 它在[0,1)范围内
# seed([x]) # 改变随机数生成器的种子seed
shuffle([1, 2, 3, 4])  # 将序列的所有元素随机排序
uniform(0, 10)  # 随机生成下一个实数 它在[x,y]范围内

# 三角函数
acos(x)  # 返回x的反余弦弧度值
asin(x, y)  # 返回x的反正弦弧度值
atan(x)  # 返回x的反正切弧度值
atan2(y, x)  # 返回给定的 X 及 Y 坐标值的反正切值
cos(x)  # 返回x的弧度的余弦值
hypot(x, y)  # 返回欧几里德范数 sqrt(x*x + y*y)
sin(x)  # 返回的x弧度的正弦值
tan(x)  # 返回x弧度的正切值
degrees(x)  # 将弧度转换为角度
radians(x)  # 将角度转换为弧度

# 数学常量
pi = pi     # 圆周率
e = e       # 自然常数
