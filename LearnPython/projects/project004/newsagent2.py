#!/usr/bin/env Python
# coding=utf-8
# @Time    : 2018/3/22 10:15
# @Author  : fanhaiyang
# @File    : newsagent2.py
# @Software: PyCharm Community Edition
# @comment : 更灵活的新闻收集代理程序

from nntplib import NNTP
from time import strftime, time, localtime
from email import message_from_string
from urllib.request import urlopen
import textwrap
import re

day = 24 * 60 * 60  # 一天


def wrap(String, max=70):
    """
        将字符串调整为最大行宽
    """
    return '\n'.join(textwrap.wrap(String)) + '\n'


class NewsAgent:
    """
    可以从新闻来源获取新闻项目并且发布到新闻目标的对象
    """

    def __init__(self):
        self.sources = []
        self.destinations = []

    def addSource(self, source):
        self.sources.append(source)

    def addDestination(self, dest):
        self.destinations.append(dest)

    def distribute(self):
        """
        从所有来源获取所有新闻项目并且发布到所有目标。
        :return:
        """
        items = []
        for source in self.sources:
            items.extend(source.getItems())  # extend把一个序列添加到列表中
        for dest in self.destinations:
            dest.receiveItems(items)


class NewsItem:
    """
    包括标题和主体文本的简单新闻项目
    """

    def __init__(self, title, body):
        self.title = title
        self.body = body


class NNTPSource:
    """
    从NNTP组中获取新闻项目的新闻来源
    """

    def __init__(self, servername, group, window):
        self.servername = servername
        self.group = group
        self.window = window
        """
        书中原getItems代码,newnews方法有问题
        """

    # def getItems(self):
    #     start=localtime(time()-self.window*day)
    #     date=strftime('%y%m%d',start)
    #     hour=strftime('%H%M%S',start)
    #     server=NNTP(self.servername)
    #     ids=server.newnews(self.group,date,hour)[1]
    #     for id in ids:
    #         lines=self.article(id)[3]
    #         message=message_from_string('\n'.join(lines))
    #
    #         title=message['subject']
    #         body=message.get_payload()
    #         if message.is_multipart():
    #             body=body[0]
    #         yield NewsItem(title,body)
    #     server.quit()
    """
    http://blog.csdn.net/hellodrawing/article/details/69939544
    从上面的博客中看到的替换代码
    """

    def getItems(self):
        server = NNTP(self.servername)
        (resp, count, first, last, name) = server.group(self.group)
        (resp, subs) = server.xhdr('subject', (str(first) + '-' + str(last)))
        for subject in subs[-10:]:
            title = subject[1]
            (reply, (num, id, list)) = server.body(subject[0])
            # list是一个列表，但是是bytes编码的，需要把每一个元素都解码成string
            body=[]
            #print(list)
            for l in list:
                body.append(l.decode('gbk')) # 注意，这里用utf-8解码会出现解码错误
            #print(body)
            body = ''.join(body)
            yield NewsItem(title, body)
        server.quit()


class SimpleWebSource:
    """
    使用正则表达式从网页总新闻项目额新闻来源
    """

    def __init__(self, url, titlePattern, bodyPattern):
        self.url = url
        self.titlePattern = re.compile(titlePattern)
        self.bodyPattern = re.compile(bodyPattern)

    def getItems(self):
        text = urlopen(self.url).read()
        text=text.decode('utf-8') # python3要加上这一句
        titles = self.titlePattern.findall(text)
        bodies = self.bodyPattern.findall(text)
        for title, body in list(zip(titles, bodies)):
            yield NewsItem(title, wrap(body))


class PlainDestination:
    """
    将所有新闻项目格式化为纯文本的新闻目标类
    """

    def receiveItems(self, items):
        for item in items:
            print(item.title)
            print('-' * len(item.title))
            print(item.body)


class HTMLDestination:
    """
    将所有新闻格式化为HTML的目标类
    """

    def __init__(self, filename):
        self.filename = filename

    def receiveItems(self, items):
        out = open(self.filename, 'w')
        print("""
         <html>
          <head>
            <title>Today's News</title>
          </head>
          <body>
          <h1>Today's News</h1>
        """, file=out)

        print('<ul>', file=out)
        id = 0
        for item in items:
            id += 1
            print('  <li><a href="#%i">%s</a></li>' % (id, item.title), file=out)
        print('</ul>', file=out)

        id = 0
        for item in items:
            id += 1
            print('<h2><a name="%i">%s</a></h2>' % (id, item.title), file=out)
            print('<pre>%s</pre>' % item.body, file=out)

        print("""
          </body>
        </html>
        """, file=out)


def runDefaultSetup():
    """
    来源和目标的默认设置。可以自己修改。
    """
    agent = NewsAgent()
    # 从BBS新闻站获取新闻的SimpleWebSource
    bbc_url = 'http://news.bbc.co.uk/text_only.stm'
    bbc_title = r'(?s)a href="[^"]*">\s*<b>\s*(.*?)\s*</b>'
    bbc_body = r'(?s)</a>\s*<br />\s*(.*?)\s*<'
    bbc = SimpleWebSource(bbc_url, bbc_title, bbc_body)

    agent.addSource(bbc)

    # 从 comp.lang.python.annouce获取新闻的NNTPSource
    clpa_server = 'web.aioe.org'
    clpa_group = 'comp.lang.python.announce'
    clpa_window = 1
    clpa = NNTPSource(clpa_server, clpa_group, clpa_window)

    agent.addSource(clpa)

    # 增加纯文本目标和HTML目标
    agent.addDestination(PlainDestination())
    agent.addDestination(HTMLDestination('news.html'))

    # 发布新闻项目
    agent.distribute()


if __name__ == '__main__':
    runDefaultSetup()
