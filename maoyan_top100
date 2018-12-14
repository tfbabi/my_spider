# -*- coding: utf-8 -*-
# @Time    : 2018/10/29 23:04
# @Author  : yannis
# @Email   : tfbabi@163.com
# @File    : Top100.py
# @Software: PyCharm
#encoding:utf-8
import requests
from requests.exceptions import RequestException
import re
import json
import os
from common_mode.log_demo import Advanced_Usage
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_one_page(url):
    '''
    获取网页html内容并返回
    '''
    head={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36','Referer':'http://www.mzitu.com/'}
    try:
        # 获取网页html内容
        response = requests.get(url,headers=head)
        # 通过状态码判断是否获取成功
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None


def get_rank_info(html,base_url="http://maoyan.com"):
    '''
    解析HTML代码，提取有用信息并返回
    '''
    # 正则表达式进行解析
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?href="(.*?)".*?data-src="(.*?)".*?name">'
        + '<a.*?>(.*?)</a>.*?"star">(.*?)</p>.*?releasetime">(.*?)</p>'
        + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    # 匹配所有符合条件的内容
    items = re.findall(pattern, html)
    for item in items:
        yield {
            'index': item[0],
            'm_url': base_url+item[1],
            'image': item[2],
            'title': item[3],
            'actor': item[4].strip()[3:],
            'time': item[5].strip()[5:],
            'score': item[6] + item[7]
        }
def get_movie_brief_introduction(movie_html):
    pattern=re.compile('<meta.*?"description".*?content="(.*?)">',re.S)
    brif=re.findall(pattern,movie_html)
    return brif
def get_movie_comment(m_html):
    pattern=re.compile('class="main">.*?"name">(.*?)</span>.*?class="time".*?title="(.*?)">.*?comment-content">(.*?)</div>',re.S)
    comment=re.findall(pattern,m_html)
    return comment
def write_to_file(content,file="movie_rank_info.txt"):
    with open(file,'a+') as f :
        if isinstance(content,dict):
            f.write(json.dumps(content,encoding="UTF-8", ensure_ascii=False)+'\r\n')
            f.close()
        else:
            f.write(content+"\n")
            f.close()
def save_move_image(img_url,save_path):
    img_content=requests.get(img_url)
    if img_content.status_code == 200:
        with open(save_path,'wb') as f:
            f.write(img_content.content)
            f.close()
def main():
    maoyan_logger=Advanced_Usage.Logging().My_Logger('maoyan_info.log')
    if not os.path.exists('covers'):
        os.mkdir('covers')
    for x in range(10):
        page_num=x*10
        url = 'http://maoyan.com/board/4?offset='+str(page_num)
        html = get_one_page(url)
        split="==="*70
        for item in get_rank_info(html):
            introduce=get_movie_brief_introduction(get_one_page(item['m_url']))
            jianjie=get_movie_comment(get_one_page(item['m_url']))
            maoyan_logger.info(item)
            #print json.dumps(item, encoding="UTF-8", ensure_ascii=False)
            write_to_file(item)
            write_to_file("".join(introduce)+'\r\n'+split,file='covers/'+'%03d'%int(item['index'])+item['title'] + '.txt')

            for user in jianjie:
                user_info="用户名:"+user[0]+'\n'+"发表时间:"+user[1]+'\n'"评论详情:"+user[2]+'\n'+split
                maoyan_logger.info(user_info)
                write_to_file(user_info,file='covers/'+'%03d'%int(item['index'])+item['title'] + '.txt')
            save_move_image(item['image'],'covers/' + '%03d'%int(item['index'])+item['title'] + '.jpg')
if __name__ == '__main__':
    main()
    #url = 'http://maoyan.com/board/4'
    #html = get_one_page(url)
    #print html
