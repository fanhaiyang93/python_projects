#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 9:37
# @Author  : fanhaiyang
# @File    : hello_reportlab.py
# @Software: PyCharm Community Edition
# @comment : 一个简单的reportlab程序
from reportlab.graphics.shapes import Drawing, String
from reportlab.graphics import renderPDF

d = Drawing(100, 100)  # 使用drawing画一个给定大小的画布
s = String(50, 50, 'Hello,World!', textAnchor='middle')  # 创建一个String对象，包括：位置，文本，其他参数
d.add(s)  # 把对象添加到画布中
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')  # 把d添加到当前目录下的hello.pdf的文件中
