#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/19 14:30
# @Author  : fanhaiyang
# @File    : pagemaker.py
# @Software: PyCharm Community Edition
# @comment : 简单的页面创建程序脚本
from xml.sax.handler import ContentHandler
from xml.sax import parse


class PageMaker(ContentHandler):
    passthrough = False

    def startElement(self, name, attrs):
        if name == 'page':
            self.passthrough = True
            self.out = open(attrs['name'] + '.html', 'w')  # 在page元素的开始处，使用给定的文件名打开一个新文件
            # 写入合适的HTML首部，包括给定的标题
            self.out.write('<html><head>\n')
            self.out.write('<title>%s</title>\n' % attrs['title'])
            self.out.write('</head><body>\n')
        elif self.passthrough:  # 在page的内部时，跳过所有的标签和字符，不修改，直接写入文件中
            self.out.write('<' + name)
            for key, val in attrs.items():
                self.out.write(' %s="%s"' % (key, val))
            self.out.write('>')

    def endElement(self, name):
        if name == 'page':  # 当在page元素结束的位置是，写入html的页脚，然后关闭文件
            self.passthrough = False
            self.out.write('\n</body></html>\n')
            self.out.close()
        elif self.passthrough:  # 不在page元素内部时，忽略所有标签
            self.out.write('</%s>' % name)

    def characters(self, chars):
        if self.passthrough: self.out.write(chars)


parse('website.xml', PageMaker())
