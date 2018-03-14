#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 22:17
# @Author  : fanhaiyang
# @File    : demo.py
# @Software: PyCharm Community Edition
# @comment : 爬虫demo
import urllib.request

width = 200
length = 200
for width in range(200, 500, 20):
    for length in range(200, 500, 20):
        url = "http://placekitten.com/g/" + str(width) + '/' + str(length)
        response = urllib.request.urlopen(url)
        cat_img = response.read()
        with open('cat_' + str(width) + '_' + str(length) + '.jpg', 'wb') as f:
            f.write(cat_img)
