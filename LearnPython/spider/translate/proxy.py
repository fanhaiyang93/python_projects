#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 16:09
# @Author  : fanhaiyang
# @File    : proxy.py
# @Software: PyCharm Community Edition
# @comment : 代理
import urllib.request

url="http://www.whatismyip.com.tw"
proxy_support=urllib.request.ProxyHandler({'http':'125.94.0.252:8080'})
openner=urllib.request.build_opener(proxy_support)
openner.add_handler= ("User-Agent",
                                  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
urllib.request.install_opener(openner)
response=urllib.request.urlopen(url)
html=response.read().decode('utf-8')
print(html)