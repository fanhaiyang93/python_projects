#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/18 12:04
# @Author  : fanhaiyang
# @File    : HeadlineHandler.py
# @Software: PyCharm Community Edition
# @comment : 创建简单的内容处理器

from xml.sax.handler import ContentHandler
from xml.sax import parse


class TestHandler(ContentHandler):  # ContentHandler的子类
    def startElement(self, name, attrs):  # 覆写startElement方法
        print(name, attrs.keys())


#parse('website.xml', TestHandler())


class HeadlineHandler(ContentHandler):
    in_headline = False

    def __init__(self, headlines):
        ContentHandler.__init__(self)
        self.headlines = headlines
        self.data = []

    def startElement(self, name, attrs):
        if name == 'h1':
            self.in_headline = True

    def endElement(self, name):
        if name == 'h1':
            text = ''.join(self.data)
            self.data = []
            self.headlines.append(text)
            self.in_headline = False

    def characters(self, string):
        if self.in_headline:
            self.data.append(string)


headlines = []
parse('website.xml', HeadlineHandler(headlines))
print('The following <h1> elements were found:')
for h in headlines:
    print(h)
