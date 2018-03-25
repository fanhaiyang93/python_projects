#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 10:03
# @Author  : fanhaiyang
# @File    : usa_gov3.py
# @Software: PyCharm Community Edition
# @comment : 使用pandas对时区进行计数
import json
from pandas import DataFrame
import matplotlib.pyplot as plt

path = '../usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]  # 列表推导式,records中每一个元素就是一行数据
frame = DataFrame(records)  # 从一组原始记录中创建DataFrame
# DataFrame是pandas中最重要的数据结构，它用于将数据表示为一个表格。数据中的一行就是表格的一行，字段就是一列
# print(frame)

series = frame['tz']  # 返回一个Series对象，类似于表格中的一列
# Series对象中有一个value_counts方法
tz_counts = series.value_counts()
print(tz_counts[:10])  # 这就是我们要的出现次数前10的时区数据

"""
接下来我们要用matplotlib为这段数据生成一个图片
"""
# 首先要把未知或缺失的时区填上一个替代值，使用fillna函数可以替换缺失值，未知值（空字符串）可以通过布尔型数组索引加以替换
clean_tz = series.fillna('Missing')
clean_tz[clean_tz == ''] = 'Unkown'  # 注意这个的用法
tz_counts=clean_tz.value_counts()
print(tz_counts[:10])
# 使用tz_counts对象的plot方法，即可得到一张水平条形图

tz_counts[:10].plot(kind='barh',rot=0) # 这这里没效果
# 应为要用Ipython 并且要以pylab模式打开，Ipython --pylab
# 解决：https://www.cnblogs.com/l33klin/p/5301303.html
plt.show() # 前面导入import matplotlib.pyplot as plt ，加上这一句，就可以直接出图了