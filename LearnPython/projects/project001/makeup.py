#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 20:05
# @Author  : fanhaiyang
# @File    : makeup.py
# @Software: PyCharm Community Edition
# @comment : 主程序，核心类。它使用一个处理程序，一些列规则和过滤器将纯文本转换成标记文件（这里指html）
# 它需要一个负责创建的构造器，一个添加规则的方法，一个添加过滤器的方法，以及一个对给定文件进行语法分析的方法
import sys, re
from handlers import *
from util import *
from rules import *




class Parser:
    """
    A parser reads a text file,applying rules and controlling a handler.
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)

        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    A specific Parser that adds rules and filters in its constructor
    """

    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')


if __name__=='__main__':
    handler = HTMLRenderer()
    parser = BasicTextParser(handler)
    parser.parse(sys.stdin)

