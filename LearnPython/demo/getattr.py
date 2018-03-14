#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 9:59
# @Author  : fanhaiyang
# @File    : get.py
# @Software: PyCharm Community Edition
# @comment : 理解getattr的用法
class A():
    a = 1

    def b(self):
        print('get 3 by getattr')


def test():
    test = A()
    # getattr可以返回对象（第一个参数）中定义的属性（第二个参数），包括变量和方法，如果没有定义可以添加默认值（第三个参数）
    print(getattr(test, 'a'))
    print(getattr(test, 'c', 2))
    method_b = getattr(test, 'b')
    if callable(method_b): method_b() # callable()函数用于检查一个对象是否时刻调用的
    # callable 对于函数, 方法, lambda 函式, 类, 以及实现了 __call__ 方法的类实例, 它都返回 True。


if __name__ == '__main__':
    test()
