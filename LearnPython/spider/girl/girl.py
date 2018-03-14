#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 16:20
# @Author  : fanhaiyang
# @File    : girl.py
# @Software: PyCharm Community Edition
# @comment : 下载煎蛋妹子图
import urllib.request
import os
import random

def url_open(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
    req = urllib.request.Request(url=url, headers=headers)
    response=urllib.request.urlopen(req)
    # proxies = ['60.12.126.140:8080',
    #            '111.178.233.35:8081',
    #            '183.232.185.177:80',
    #            '218.92.220.17:8080'
    #            ]
    # proxy = random.choice(proxies)
    # proxy_support = urllib.request.ProxyHandler({'http': proxy})
    # oppenr = urllib.request.build_opener(proxy_support)
    # urllib.request.install_opener(oppenr)
    html = response.read()
    return html


def get_page(url):
    html = url_open(url).decode('utf-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)
    return html[a:b]


def find_imgs(url):
    html = url_open(url).decode('utf-8')
    print(html)
    img_addrs = []
    a = html.find('img src=')
    print(a)
    while a != -1:
        b = html.find('.jpg', a, a + 255)
        print(b)
        if b != -1:
            img_addrs.append(html[a + 9:b + 4])
        else:
            b = a + 9
        a = html.find('img src=', b)

    return img_addrs


def save_imgs(folder, img_addrs):
    for each in img_addrs:
        filename = each.split('/')[-1]
        with open(filename, 'wb') as f:
            img = url_open(each)
            f.write(img)


def download_girl(folder="girls", pages=1):
    #os.mkdir(folder)
    os.chdir(folder)
    url = "http://jandan.net/ooxx/"
    page_num = int(get_page(url))

    for i in range(pages):
        page_num -= i
        page_url = url + 'page-' + str(page_num) + '#comments'
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    download_girl()
