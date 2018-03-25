#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/23 9:26
# @Author  : fanhaiyang
# @File    : usa_gov.py
# @Software: PyCharm Community Edition
# @comment : 来自bit.ly的1.usa.gov数据。初识数据
# 数据已经下载好了
path='../usagov_bitly_data2012-03-16-1331923249.txt'
# 打印一行数据，数据是json格式
# 格式化后，用的nodepad++
"""
{
	"a": "Mozilla\/5.0 (Windows NT 6.1; WOW64) AppleWebKit\/535.11 (KHTML, like Gecko) Chrome\/17.0.963.78 Safari\/535.11",
	"c": "US",
	"nk": 1,
	"tz": "America\/New_York",
	"gr": "MA",
	"g": "A6qOVH",
	"h": "wfLQtf",
	"l": "orofrog",
	"al": "en-US,en;q=0.8",
	"hh": "1.usa.gov",
	"r": "http:\/\/www.facebook.com\/l\/7AQEFzjSi\/1.usa.gov\/wfLQtf",
	"u": "http:\/\/www.ncbi.nlm.nih.gov\/pubmed\/22415991",
	"t": 1331923247,
	"hc": 1331822918,
	"cy": "Danvers",
	"ll": [42.576698,-70.954903]
}
"""
print(open(path).readline())
