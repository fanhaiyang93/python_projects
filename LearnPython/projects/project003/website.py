#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 15:11
# @Author  : fanhaiyang
# @File    : website.py
# @Software: PyCharm Community Edition
# @comment : 完整实现。调度程序的混入类
"""
与其在标准的泛型事件处理程序（比如startElement）中编写大量的if语句，还不如编写自己的具体程序（比如startPage），
并且自动调用他们。混入类可以实现这个功能，然后将这个类和CintentHandler一同继承。
此外，还期望程序具备下面的功能
1. 当使用foo这样的名字调用startElement时，他会试图寻找叫做startFoo的事件处理程序，然后利用给定的特性进行调用。
2. 同样地，如果使用foo调用endElement，那么它会试着调用endFoo
3. 如果在这些方法中找不到给定的事件处理程序，那么会分别调用defaultStart或者defaultEnd方法。如果连默认的也没有的话，就什么也不做。
"""
from xml.sax.handler import ContentHandler
from xml.sax import parse
import os


# class Dispatcher:
#     def startElement(self, name, attrs):
#         self.dispatch('start', name, attrs)
#
#     def endElement(self, name):
#         self.dispatch('end', name)
#
#     def dispatch(self, prefix, name, attrs=None):
#         mname = prefix + name.capitalize()
#         dname = 'default' + prefix.capitalize()
#         method = getattr(self, mname, None)
#         if callable(method):
#             args = ()
#         else:
#             method = getattr(self, dname, None)
#             args = name, # 逗号？
#         if prefix == 'start':
#             args += attrs, #逗号？
#         if callable(method): method(*args)

class Dispatcher:

    def dispatch(self, prefix, name, attrs=None):
        mname = prefix + name.capitalize()
        dname = 'default' + prefix.capitalize()
        method = getattr(self, mname, None)
        if callable(method): args = ()
        else:
            method = getattr(self, dname, None)
            args = name,
        if prefix == 'start': args += attrs,
        if callable(method): method(*args)

    def startElement(self, name, attrs):
        self.dispatch('start', name, attrs)

    def endElement(self, name):
        self.dispatch('end', name)


class WebsiteConstructor(Dispatcher, ContentHandler):
    passthrough = False

    def __init__(self, directory):
        self.directory = [directory]
        self.ensureDirectory()

    def ensureDirectory(self):
        path = os.path.join(*self.directory)
        if not os.path.isdir(path): os.makedirs(path)

    def characters(self, chars):
        if self.passthrough: self.out.write(chars)

    def defaultStart(self, name, attrs):
        if self.passthrough:
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' %s="%s"' % (key, val))
            self.out.write('>')

    def defaultEnd(self, name):
        if self.passthrough:
            self.out.write('</%s>' % name)

    def startDirectory(self, attrs):
        self.directory.append(attrs['name'])
        self.ensureDirectory()

    def endDirectory(self):
        self.directory.pop()

    def startPage(self, attrs):
        filename = os.path.join(*self.directory + [attrs['name'] + '.html'])
        self.out = open(filename, 'w')
        self.writeHeader(attrs['title'])
        self.passthrough = True

    def endPage(self):
        self.passthrough = False
        self.writeFooter()
        self.out.close()

    def writeHeader(self, title):
        self.out.write('<html>\n<head>\n  <title>')
        self.out.write(title)
        self.out.write('</title>\n </head>\n <body>\n')

    def writeFooter(self):
        self.out.write('\n</body>\n</html>\n')


parse('website.xml', WebsiteConstructor('public_html'))
