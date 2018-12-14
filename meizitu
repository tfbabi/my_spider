#!/usr/bin/python
#encoding:utf8

from multiprocessing import Pool,Manager
from multiprocessing import Process,Queue
from bs4 import BeautifulSoup
from common_mode.log_demo import Advanced_Usage
import requests
import lxml
import re
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import time

head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36','Referer':'http://www.mzitu.com/'}
meizi_logger=Advanced_Usage.Logging().My_Logger('meizitu_download.log')
u="http://www.mzitu.com/"
html = requests.get(u,headers=head)
soup = BeautifulSoup(html.text,'lxml')
max_page =soup.find('div',class_='nav-links').find_all('a')[-2]['href'].split('/')[-2].strip()
def getPic(p):
    url="http://www.mzitu.com/page/"+str(p)
    n_html = requests.get(url,headers=head)
    #print n_html.text
    n_soup = BeautifulSoup(n_html.text,'lxml')
    name = n_soup.find('ul',id='pins').find_all('li')

    for x in name:
        mmurl = x.a['href']
        mmtxt = x.a.img['alt']
        mm_time = x.span.next_sibling.text
        mm_count=x.span.next_sibling.next_sibling.text
        mmhtml=requests.get(mmurl,headers=head)
        mmsoup=BeautifulSoup(mmhtml.text,'lxml')
        mm_max_page=mmsoup.find('div',class_='pagenavi').find_all('a')[-2].span.text.strip()
        base_path='D:\mm2018'
#        end_path=path = '['+mm_time+']'+'['+mm_count+']'+'['+mmtxt.strip()+']'
        end_path = '['+mm_time+']'+'['+mmtxt.strip()+']'
        end_path2 = '['+mm_time+']'+'['+re.sub('[?:"]','',mmtxt.strip()).split()[0]+']'
        dest_path=os.path.join(base_path,end_path).strip()
        dest_path2=os.path.join(base_path,end_path2).strip()
        if not os.path.exists(dest_path):
            try:
                os.mkdir(dest_path.strip())
                meizi_logger.info("第%s页!%s文件夹创建成功!开始下载这个MM的美图..." %(p,dest_path))
                os.chdir("D:\mm2018\\"+end_path.strip())
            except Exception,e:
                meizi_logger.warn(end_path2)
                if os.path.exists(dest_path2.strip()):
                    meizi_logger.warn("第%s页! 更新时间%s:浏览量:%s %s已存在!，特殊文件夹!不用重复创建了." %(p,mm_time,mm_count,mmtxt))
                    continue
                else:
                    os.mkdir(dest_path2.strip())
                    meizi_logger.info("第%s页!%s文件夹创建成功!开始下载这个MM的美图..." %(p,dest_path))
                    os.chdir("D:\mm2018\\"+end_path2.strip())
                    meizi_logger.warn(Exception,":",e)
            for img_page in range(1,int(mm_max_page)+1):
                img_url=mmurl+'/'+str(img_page)
                img_html=requests.get(img_url,headers=head)
                img_soup=BeautifulSoup(img_html.text,'lxml')
                dest_url=img_soup.find('div',class_='main-image').find_all('img')[-1]['src']
                img_name=dest_url.split('/')[-1]
                dest_img = requests.get(dest_url, headers=head)
                f = open(img_name,'ab')
                f.write(dest_img.content)
                f.close()
                meizi_logger.info("第%s张，%s图片下载成功!" %(img_page,dest_url))
            meizi_logger.info("%s 新一期下载完毕，继续下一位..." %dest_path)
        else:
            meizi_logger.info("第%s页! 更新时间%s:浏览量:%s %s已存在! 跳过......" %(p,mm_time,mm_count,mmtxt))
            continue



if __name__ == "__main__":

    pool=Pool(3)
    for page in range(1,int(max_page)+1):
        pool.apply_async(getPic,(page,))
    #p=Process(target=getPic,args=(max_page,))
    pool.close()
    pool.join()
    #p.start()
    #p.join()
