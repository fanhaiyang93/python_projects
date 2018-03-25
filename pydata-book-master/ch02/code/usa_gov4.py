#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 10:42
# @Author  : fanhaiyang
# @File    : usa_gov4.py
# @Software: PyCharm Community Edition
# @comment :
import json
from pandas import DataFrame,Series
import numpy as np
import matplotlib.pyplot as plt

path = '../usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]  # 列表推导式,records中每一个元素就是一行数据
frame = DataFrame(records)  # 从一组原始记录中创建DataFrame
# 字段'a'
# print(frame['a'][0]) # Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.78 Safari/535.11
results=Series([x.split()[0] for x in frame.a.dropna()]) #截取第一节，对应浏览器信息，并转成Series对象。
# print(results.value_counts()[:8])

"""
现在我们想按windows用户和非windows用户对时区统计信息进行分解。
我们认为，只要agent（’a‘）字段中含有“Windows”就认为是windows用户
"""
cframe=frame[frame.a.notnull()] # 去掉缺失值
opearing_system=np.where(cframe['a'].str.contains('Windows'),'Windows','not Windows')# 根据a值计算出各行是否是Windows
# print(opearing_system[:10])
# 接下来根据时区和新得到的操作系统列表对数据进行分组
by_tz_os=cframe.groupby(['tz',opearing_system]) # 靠什么连接起来的？？
# 通过size对分组进行计数，并用unstack对计数结果进行重塑
agg_counts=by_tz_os.size().unstack().fillna(0)
# print(agg_counts[:10])

indexer=agg_counts.sum(1).argsort() # 用于按升序排序？？？
# print(indexer[:10])
# 然后通过take按照这个顺序截取最后10行
count_subset=agg_counts.take(indexer)[-10:]
# print(count_subset)

# 生成条形图
count_subset.plot(kind='barh',stacked=True)
#plt.show()

# 将各行规范化为"总计为1"，并重新绘图
normed_subset=count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind='barh',stacked=True)
plt.show()