#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 10:10
# @Author  : fanhaiyang
# @File    : test_mix_class.py
# @Software: PyCharm Community Edition
# @comment : 多继承的类查找方式，混入类
class A:
    def method(self):
        print('from A')
    def methodA(self):
        print('A')
class B:
    def method(self):
        print('from B')
    def methodB(self):
        print('B')

class C(A,B):
    pass

class D(B,A):
    pass

if __name__=='__main__':
    c=C()
    c.method()
    c.methodA()
    c.methodB()
    d=D()
    d.method()
    d.methodA()
    d.methodB()