#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 9:21
# @Author  : fanhaiyang
# @File    : simple_draw.py
# @Software: PyCharm Communit Edition
# @comment : 初步实现画幅好画


from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.lib import colors

# 造几个数据先
data = [
    # year,month,predicted,high,low
    (2007, 8, 113.2, 114.2, 112.2),
    (2007, 9, 112.8, 115.8, 109.8),
    (2007, 10, 111.0, 116.0, 106.0),
    (2007, 11, 109.8, 116.8, 102.8),
    (2007, 12, 107.3, 115.3, 99.3),
    (2008, 1, 105.2, 114.2, 96.2),
    (2008, 2, 104.1, 114.1, 94.1),
    (2008, 3, 99.0, 110.9, 88.9),
]

drawing = Drawing(200, 150)

pred = [row[2] - 40 for row in data]
high = [row[3] - 40 for row in data]
low = [row[4] - 40 for row in data]
times = [200 * ((row[0] + row[1] / 12.0) - 2001) - 110 for row in data]
# python3里zip函数，返回的不再是一个列表，而是个zip对象，需要用list转成list列表
line1 = PolyLine(list(zip(times, pred)), strokeColor=colors.blue) # 画不出折线图！！！！？？？
line2 = PolyLine(list(zip(times, high)), strokeColor=colors.red)
line3 = PolyLine(list(zip(times, low)), strokeColor=colors.green)
drawing.add(line1)
drawing.add(line2)
drawing.add(line3)
drawing.add(String(65, 115, 'Sunspots', fontSize=18, fillColor=colors.green))

renderPDF.drawToFile(drawing, 'report1.pdf', 'Sunspots')
