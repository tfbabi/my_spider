# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 20:16
# @Author  : yannis
# @Email   : tfbabi@163.com
# @File    : spider.py
# @Software: PyCharm

from common_mode.log_demo import Advanced_Usage
import requests
import re
from bs4 import BeautifulSoup
from lxml import etree
import sys
reload(sys)
import json

head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36','Referer':'http://tieba.baidu.com/p/3993051268'}

def getSiteContent(url):
    html=requests.get(url,headers=head)
    return html.content.decode('utf-8')

html=getSiteContent("http://tieba.baidu.com/p/5911119735")
selector=etree.HTML(html)
max_page=selector.xpath('//div[@class="pb_footer"]/div/div/ul/li[2]/span[2]/text()')[0]
for page in range(1,int(max_page)+1):
    url="http://tieba.baidu.com/p/5911119735?pn=%s" %page
    html=getSiteContent(url)
    selector=etree.HTML(html)

    print "第%d页" %page+"****"*50
    log=selector.xpath('//div[starts-with(@class,"l_post ")]/@data-field')    #start-with   xpath高级用法
    for each in log:
        each=json.loads(each)
        if not each["author"].has_key("level_name"):     #过滤广告推广
            print "这是一个广告"
            continue            #跳出本次循环  break跳出所有循环
        userid=each['author']['user_id']
        username=each['author']['user_name']
        level_name=each['author']['level_name']
        post_id=each['content']['post_id']
        level_id=each['author']['level_id']
        post_no=each['content']['post_no']
        date=each['content']['date']

        print u"用户名:%s" %username
        print u"贴吧段位:%s" %level_name
        print u"Post_id:%s" %post_id
        print u"贴吧等级:%s" %level_id
        print u"楼层数:%s" %post_no
        print u"发表时间:%s" %date
        print ">>>"*40
