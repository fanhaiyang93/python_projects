#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 22:55
# @Author  : fanhaiyang
# @File    : translate.py
# @Software: PyCharm Community Edition
# @comment : 有道翻译,没有成功
import urllib.request
import urllib.parse
import json

def main():
    while True:
        content=input("请输入需要翻译的内容（退出输入q）：")
        if content in ("Q","q","quit"):
            break
        else:
            url="http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=null"
            data={}
            data["type"]="AUTO"
            data["i"] = content
            data["doctype"] = "json"
            data["xmlVersion"] = "1.8"
            data["keyfrom"] = "fanyi.web"
            data["ue"] = "utf-8"
            data["action"] = "FY_BY_CLICKBUTTON"
            data["typoResult"] = "true"
            data=urllib.parse.urlencode(data).encode("utf-8")

            #百度搜索免费代理IP即可
            proxy_support = urllib.request.ProxyHandler({"http": "115.223.217.118:9000"})
            opener = urllib.request.build_opener(proxy_support)
            opener.add_header = ("User-Agent",
                                  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36")
            urllib.request.install_opener(opener)

            req = urllib.request.Request(url,data)
            response = urllib.request.urlopen(req)
            html = response.read().decode("utf-8")

            target=json.loads(html)
            print("翻译的结果为：%s" %(target["translateResult"][0][0]["tgt"]))

if __name__=="__main__":
    main()