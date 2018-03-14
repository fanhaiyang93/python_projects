#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 19:04
# @Author  : fanhaiyang
# @File    : simple_markup.py
# @Software: PyCharm Community Edition
# @comment : 简单实现，添加一些标记
import sys, re

# sys.path.append(r"E:\python\learnPython\project001")
# print(sys.path)
'''
pycharm不会将当前文件目录自动加入自己的sourse_path。导入同级目录的模块时会提示错误，但是可以正常运行
右键make_directory as-->Sources Root将当前工作的文件夹加入source_path就可以去掉错误提示。
'''
from util import blocks

print('<html><head><title>...</title><body>')

title = True
for block in blocks(sys.stdin):
    block = re.sub(r'\*(.+?)\*', r'<em>\1</em>', block)
    if title:
        print('<h1>')
        print(block)
        print('</h1>')
        title = False
    else:
        print('<p>')
        print(block)
        print('</p>')
print('</body></html>')

# 用命令行运行：python simple_markup.py < test_input.txt > test_output.html，生成test_output.html文件，在浏览器中看效果
