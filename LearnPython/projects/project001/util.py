#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/11 17:05
# @Author  : fanhaiyang
# @File    : util.py
# @Software: PyCharm Community Edition
# @comment : 文本块生成器，把文本切分成段落



def lines(file):  # lines生成器，在文件的最后追加一个空行
    for line in file:
        yield line
    yield '\n'


def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


def test():
    with open('test_input.txt', 'r') as file:
        for block in blocks(file):
            print(block)


if __name__ == "__main__":
    test()
