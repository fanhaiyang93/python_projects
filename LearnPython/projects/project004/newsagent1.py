#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 13:22
# @Author  : fanhaiyang
# @File    : newsagent1.py
# @Software: PyCharm Community Edition
# @comment : 简单的新闻收集代理程序
from nntplib import NNTP
from time import strftime, time, localtime


# day = 24 * 60 * 60  # one day
# yesterday = localtime(time() - day)
# date = strftime('%y%m%d', yesterday)
# hour = strftime('%H%M%S', yesterday)
# servername = 'web.aioe.org'
# group = 'comp.lang.python.announce'
# server = NNTP(servername)
# ids = server.newnews(group, date,hour)[1] # 该方法有问题
# for id in ids:
#     print(id)
#     head = server.head(id)[3]
#     for line in head:
#         if line.lower().startswith('subject:'):
#             subjucet = line[9:]
#             break
#         body = server.body(id)[3]
#
#         print(subjucet)
#         print('-' * len(subjucet))
#         print('\n'.join(body))

servername = 'web.aioe.org'
group = 'comp.lang.python.announce'
server = NNTP(servername)
(resp, count, first, last, name) = server.group(group)
(resp, subs) = server.xhdr('subject', (str(first) + '-' +(last)))
for subject in subs[-10:]:
    title = subject[1]
    (reply, num, id, list) = server.body(subject[0])
    body = ''.join(list)
    print(num) #186919
    print(title) #Re: Find out which module a class came from
    print(''.join(list))#prano wrote:> But for merely ordinary obfuscation caused by poor...

server.quit()

