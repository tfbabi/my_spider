#!/usr/bin/python
#encoding:utf8

import requests
from bs4 import BeautifulSoup
import os,re
import urllib,urllib2
head =  {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3018.3 Safari/537.36'}
for x in range(1,70):
    re_url="http://www.mmjpg.com/home/"+str(x)
    request=urllib2.Request(re_url,headers=head)
    r=urllib2.urlopen(request)
    html= r.read()
    Soup = BeautifulSoup(html,'lxml')
#   print Soup.prettify()
    li_list = Soup.find('div',class_='pic').find_all('span',class_='title')

    for li in li_list:
        title=li.get_text()
        herf=li.a['href']
        page_html = requests.get(herf, headers=head)
        html_Soup = BeautifulSoup(page_html.text, 'lxml')
        max_page = html_Soup.find('div',class_='page').find_all('a')[-2].get_text()
        base_path='E:\mm'
        end_path=path = title.strip()
        os.mkdir(os.path.join(base_path,end_path))
        os.chdir("E:\mm\\"+path)
        for page in range(1,int(max_page)+1):
            page_url = herf+'/'+str(page)
            img_html = requests.get(page_url, headers=head)
            img_Soup = BeautifulSoup(img_html.text, 'lxml')
            img_url = img_Soup.find('div', class_='content').find('img')['src']
            name = img_url.split('/')[-1].split('.')[0]
            img = requests.get(img_url, headers=head)
            f = open(name+'.jpg', 'ab')
            f.write(img.content)
            f.close()
#            print img_url

'''
参考http://cuiqingcai.com/3179.html大神指导，第一次完整的实现图片爬取，漏洞百出，期待以后改善。
重点学习BeautifulSoup，request，re等模块使用，熟悉网页的解析方式，善于从网页中寻找有用元素。爬取思想方式很重要。
'''
