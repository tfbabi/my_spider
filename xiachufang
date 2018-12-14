# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 18:04
# @Author  : yannis
# @Email   : tfbabi@163.com
# @File    : demo.py
# @Software: PyCharm
#encoding:utf-8

import requests
from bs4 import BeautifulSoup
import  re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import json
from common_mode.db_demo.PyMysql import demo

def get_html(url,header):
    content=requests.get(url,headers=header)
    if content.status_code == 200:
        return content.text
    return None


def write_to_txt(content,path):
    with open(path,'a') as f:
        f.write(content)

header={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",'Referer': 'http://www.xiachufang.com'}


def get_food_use(url):
    html=get_html(url,header)
    pattern=re.compile('<li.*?<p.*?="text".*?>(.*?)</p>.*?alt="(.*?)".*?</li>',re.S)
    zuofa=re.findall(pattern,html)
    return zuofa
#print get_food_use("http://www.xiachufang.com/recipe/1000229/")

ruler=demo.MySQL_Utils("127.0.0.1",3306,"root","ski.root","xiaochufang")

for num in range(11):
    source_url="http://www.xiachufang.com/category/40076/?page="+str(num)
    html=get_html(source_url,header)
    pattern=re.compile('<li>.*?<div.*?="recipe.*?">.*?="(.*?)".*?alt="(.*?)".*?</li>',re.S)
    result = re.findall(pattern,html)
    for item in result:
        son_url = "http://www.xiachufang.com"+item[0]
        name = item[1]
        write_to_txt(name+'\n'+son_url+'\n','Making_method\\'+name.split('/')[0]+son_url.split('/')[-2]+'.txt')
        sql="insert into cook (cook_name,url) VALUES ('%s','%s')" %(name,son_url)
        print sql
        ruler.execute(sql)
        foo=get_food_use(son_url)
        for content in foo:
            step=content[1]
            txt=content[0]
            write_to_txt(step+'\n'+txt+'\n','Making_method\\'+name.split('/')[0]+son_url.split('/')[-2]+'.txt')
        #print name,son_url
    #print num
