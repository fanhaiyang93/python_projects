#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 9:38
# @Author  : fanhaiyang
# @File    : usa_gov2.py
# @Software: PyCharm Community Edition
# @comment : 来自bit.ly的1.usa.gov数据。使用python的json模块打开数据,并用collections模块处理时区数据

import json
path='../usagov_bitly_data2012-03-16-1331923249.txt'
# 逐行加载数据
records=[json.loads(line) for line in open(path)] # 列表推导式,records中每一个元素就是一行数据
# print(records[0])
# print(records[0]['tz'])
# tz字段指数据集的时区，现在我们想统计该数据集中最常出现的是哪个时区
"""
使用纯python代码对时区进行计数
"""
# time_zones=[rec['tz'] for rec in records] # KeyError: 'tz' 说明并不是所有的数据都有tz字段
time_zones=[rec['tz'] for rec in records if 'tz' in rec] # 加个过滤条件
print(time_zones[:10]) # 打印前十个时区，发现有些是空的，先不做处理
# 写一个方法统计每个时区出现次数
def get_counts(sequence):
    counts={} # 字典
    for x in sequence:
        if x in counts:
            counts[x]+=1
        else:
            counts[x]=1
    return counts
# 如果你对python标准库十分熟悉，那么可以简洁一点
from collections import defaultdict
def get_counts2(sequence):
    counts=defaultdict(int) #所用的值都会被初始化为0
    for x in sequence:
        counts[x]+=1
    return counts

# 现在只需要time_zones传入即可
counts=get_counts(time_zones)
print(counts['America/New_York']) # 注意是中括号
print(len(counts))
# 现在需要找出出现次数前十的时区，可以使用collections.Counter类，非常简单
from collections import Counter
counts=Counter(time_zones)
# 打印前10位的时区
print(counts.most_common(10))
