import sys
import json
import time
import requests
from datetime import datetime
from bs4 import BeautifulSoup
# 忽略requests证书警告
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



def notice(name, title):
    text = "%s SRC 有新公告" % name
    desp = '公告内容：%s' % title
    requests.get('https://sc.ftqq.com/%s.send?text=%s&desp=%s' % (key, text, desp))


def print_color(name, notice_time, title):
    grep_list = ['活动', '周岁', '周年', '双倍', '三倍', '端午', '七夕', '双11安全保卫战']
    num = 1
    for i in grep_list:
        if (i in title) and (num == 1) and ('2022' in notice_time or notice_time == '' or '22-' in notice_time) and (
                '公示' not in title and '公告' not in title):
            print('\033[0;33m| \033[0m\033[0;31m%s\t%s\033[0m' % (notice_time, title))
            num = num + 1
    if num == 1:
        print('\033[0;33m| \033[0m' + notice_time + '\t' + title)

    current_day = time.strftime("%Y-%m-%d", time.localtime())
    if current_day == notice_time:
         notice(name, title)
         time.sleep(3)


def src_360(number):
    print('\n\033[0;33m-----------------------360 SRC------------------------\033[0m')
    url = 'https://security.360.cn/News/news?type=-1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.news-content')[0].select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 4].select('.new-list-time')[0].text.strip() #匹配公告，第一条置顶公告，就是在notice_list盒子下的第四个li标签下的公告时间的div，并获取
        title = notice_list[i + 4].select('a')[0].text
        print_color('360', time, title)


def src_58(number):
    print('\n\033[0;33m-----------------------58 SRC------------------------\033[0m')
    url = 'https://security.58.com/notice/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.time')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text
        title = bs.select('.box')[0].select('a')[i].text
        print_color('58', time, title)


def alibaba(number):
    print('\n\033[0;33m-----------------------阿里SRC------------------------\033[0m')
    url = 'https://security.alibaba.com/api/asrc/pub/announcements/list.json?&page=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['lastModify'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('阿里', time, title)

def iqiyi(number):
    print('\n\033[0;33m-----------------------爱奇艺SRC----------------------\033[0m')
    url = 'https://security.iqiyi.com/api/publish/notice/list?sign=6ce5b4f7ad460b2ae3046422f61f905e4e3ecd03'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['create_time_str']
        title = notice_list[i]['title']
        print_color('爱奇艺', time, title)


def baidu(number):
    print('\n\033[0;33m-----------------------百度SRC------------------------\033[0m')
    url = 'https://bsrc.baidu.com/v2/api/announcement?type=&page=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['retdata']['announcements']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('百度', time, title)


def ke(number):
    print('\n\033[0;33m-----------------------贝壳SRC------------------------\033[0m')
    url = 'https://security.ke.com/api/notices/list'
    headers = {
        'Referer': 'https://security.ke.com/notices',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.post(url, headers=headers, data={"page": 1})
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('贝壳', time, title)


def bilibili(number):
    print('\n\033[0;33m-----------------------哔哩哔哩SRC---------------------\033[0m')
    url = 'https://security.bilibili.com/announcement/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    number = number * 2 + 1
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(2, number, 2):
        time = notice_list[i].text.replace('\n', '')
        title = notice_list[i + 1].text.replace('\n', '')
        print_color('哔哩哔哩', time, title)


def cainiao(number):
    print('\n\033[0;33m-----------------------菜鸟SRC------------------------\033[0m')
    url = 'https://sec.cainiao.com/announcement.htm'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text.split('\n')[0].strip().split('][')[0].replace('[', '')
        title = notice_list[i].text.split('\n')[1].strip()
        print_color('菜鸟', time, title)


def didichuxing(number):
    print('\n\033[0;33m-----------------------滴滴出行SRC---------------------\033[0m')
    url = 'http://sec.didichuxing.com/rest/article/list?page=1&size=5&option=0'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['time']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color('滴滴出行', time_format, title)


def duxiaoman(number):
    print('\n\033[0;33m-----------------------度小满SRC----------------------\033[0m')
    url = 'https://security.duxiaoman.com/index.php?v2api/announcelist'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='page=1&type=0&token=null')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['time']
        title = notice_list[i]['title']
        print_color('度小满', time, title)


def guaZi(number):
    print('\n\033[0;33m-----------------------瓜子SRC------------------------\033[0m')
    url = 'https://security.guazi.com/gzsrc/notice/queryNoticesList'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data="pageNo=1")
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publishDate'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('瓜子', time, title)


def jd(number):
    print('\n\033[0;33m-----------------------京东SRC------------------------\033[0m')
    url = 'https://security.jd.com/notice/list?parent_type=2&child_type=3&offset=0&limit=12'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['notices']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['CreateTime'].split(' ')[0]
        title = notice_list[i]['Title']
        print_color('京东', time, title)


def alipay(number):
    print('\n\033[0;33m-----------------------蚂蚁金服SRC---------------------\033[0m')
    url = 'https://security.alipay.com/sc/afsrc/notice/noticeList.json?_input_charset=utf-8&_output_charset=utf-8'
    headers = {
        'Referer': 'https://security.alipay.com/home.htm',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['resultAfsrc']['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['noticeTime']
        title = notice_list[i]['title']
        print_color('蚂蚁金服', time, title)


def meituan(number):
    print('\n\033[0;33m-----------------------美团SRC------------------------\033[0m')
    url = 'https://security.meituan.com/api/announce/list?typeId=0&curPage=1&perPage=5'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['items']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['createTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['name']
        print_color('美团', time_format, title)


def immomo(number):
    print('\n\033[0;33m-----------------------陌陌SRC------------------------\033[0m')
    url = 'https://security.immomo.com/api/news/blog/?page=1&type=3'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['results']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['created_at']
        title = notice_list[i]['title']
        print_color('陌陌', time, title)


def oppo(number):
    print('\n\033[0;33m-----------------------OPPO SRC-----------------------\033[0m')
    url = 'https://security.oppo.com/cn/be/cn/osrc/FEnotice/findAllNotice'
    headers = {
        'Host': 'security.oppo.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"pageNum":1,"pageSize":10,"noticeType":2}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['notice_online_time'].split(' ')[0]
        title = notice_list[i]['notice_name']
        print_color('OPPO', time, title)


def pingan(number):
    print('\n\033[0;33m-----------------------平安SRC------------------------\033[0m')
    url = 'https://security.pingan.com/announcement/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('#News_List')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 1].select('span')[0].text.strip().replace('【', '').replace('】', '')
        title = notice_list[i + 1].select('a')[0].text.strip()
        print_color('平安', time, title)


def shuidihuzhu(number):
    print('\n\033[0;33m-----------------------水滴SRC------------------------\033[0m')
    url = 'https://api.shuidihuzhu.com/api/wide/announce/getAnnouncePageList'
    headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    r = requests.post(url, headers=headers, data='{"pageNum":1,"pageSize":10}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['updateTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color('水滴', time_format, title)


def sf_express(number):
    print('\n\033[0;33m-----------------------顺丰SRC------------------------\033[0m')
    url = 'http://sfsrc.sf-express.com/notice/getLatestNotices'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data="limit=10&offset=0")
    r_json = json.loads(r.text)
    notice_list = r_json['rows']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['modifyTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['noticeTitle']
        print_color('顺丰', time_format, title)


def tencent(number):
    print('\n\033[0;33m-----------------------腾讯SRC------------------------\033[0m')
    url = 'https://security.tencent.com/index.php/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.section-announcement')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.replace('/', '-')
        title = notice_list[i].select('a')[0].text
        print_color('腾讯', time, title)


def vivo(number):
    print('\n\033[0;33m-----------------------vivo SRC-----------------------\033[0m')
    url = 'https://security.vivo.com.cn/api/front/notice/noticeListByPage.do'
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"pageNo":1,"pageSize":10,"pageOrder":"","pageSort":""}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['updateTime']
        title = notice_list[i]['noticeTitle']
        print_color('vivo', time, title)


def src_163(number):
    print('\n\033[0;33m-----------------------网易SRC------------------------\033[0m')
    url = 'https://aq.163.com/api/p/article/getNoticeList.json'
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='{"offset":0,"limit":20,"childCategory":1}')
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        timeStamp = notice_list[i]['createTime']
        time_format = time.strftime("%Y-%m-%d", time.localtime(float(timeStamp / 1000)))
        title = notice_list[i]['title']
        print_color('网易', time_format, title)


def vip(number):
    print('\n\033[0;33m-----------------------唯品会SRC----------------------\033[0m')
    url = 'https://sec.vip.com/notice'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.vsrc-news-nameLink')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = bs.select('.news-date')[0].text
        title = notice_list[i].text
        print_color('唯品会', time, title)


def wifi(number):
    print('\n\033[0;33m-----------------------WiFi万能钥匙SRC-----------------\033[0m')
    url = 'https://sec.wifi.com/api/announce'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers, data='pageNo=0&limit=10')
    r_json = json.loads(r.text)
    notice_list = r_json['data']['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publish_time'].split(' ')[0]
        title = notice_list[i]['title']
        print_color('WiFi万能钥匙', time, title)


def zto(number):
    print('\n\033[0;33m-----------------------中通SRC------------------------\033[0m')
    url = 'https://sec.zto.com/api/notice/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['updated_at'].split('.')[0].replace('T', ' ').split(' ')[0]
        title = notice_list[i]['title']
        print_color('中通', time, title)


def bytedance(number):
    print('\n\033[0;33m-----------------------字节跳动SRC---------------------\033[0m')
    url = 'https://src.bytedance.com/notice/getNotices/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.container')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.split(' ')[0].replace('年', '-').replace('月', '-').replace('日', '')
        title = notice_list[i].select('a')[0].text
        print_color('字节跳动', time, title)

def bigo(number):
    print('\n\033[0;33m-----------------------bigo SRC------------------------\033[0m')
    url = 'https://security.bigo.sg/announcements/allabstract'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['release_time'].split("T",maxsplit=1)[0]
        title = notice_list[i]['chinese_title']
        print_color('bigo', time, title)

def boss(number):
    print('\n\033[0;33m-----------------------boss SRC------------------------\033[0m')
    url = 'https://src.zhipin.com/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.section_announcement')[0].select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.strip() #匹配公告，第一条置顶公告，就是在notice_list盒子下的第四个li标签下的公告时间的div，并获取
        title = notice_list[i].select('a')[0].text
        print_color('boss', time, title)

def dfcf(number):
    print('\n\033[0;33m-----------------------东方财富 SRC------------------------\033[0m')
    url = 'https://security.eastmoney.com/news'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.content-bd')[0].select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.strip() #匹配公告，第一条置顶公告，就是在notice_list盒子下的第四个li标签下的公告时间的div，并获取
        title = notice_list[i].select('a')[0].text.strip().replace(" ","").replace("\n","").replace("\r","").replace("置顶","")
        print_color('东方财富', time, title)

def fuYou(number):
    print('\n\033[0;33m-----------------------富友 SRC------------------------\033[0m')
    url = 'https://fsrc.fuiou.com/notice/getNoticeData.action'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['results']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTimeStr'].split("T",maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('富友', time, title)

def huoLala(number):
    print('\n\033[0;33m-----------------------货拉拉 SRC------------------------\033[0m')
    url = 'https://llsrc.huolala.cn/api/v1/notices?pageIndex=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['created_at'].split()[0]
        title = notice_list[i]['notice_name']
        print_color('货拉拉', time, title)

def jiaoDian(number):
    try:
        print('\n\033[0;33m-----------------------焦点 SRC------------------------\033[0m')
        url = 'https://security.focuschina.com/home/announcement.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'html.parser')
        notice_list = bs.select('.anno-lst')[0].select('li') #匹配到盒子里边的所有li标签
        if number > len(notice_list):
            number = len(notice_list)
        for i in range(0, number):
            time = notice_list[i].select('.anno-lst-date')[0].text.strip() #匹配公告，第一条置顶公告，就是在notice_list盒子下的第四个li标签下的公告时间的div，并获取
            title = notice_list[i].select('.anno-lst-cons')[0].select('a')[1].text.strip().replace(" ","").replace("\n","").replace("\r","").replace("置顶","")
            print_color('焦点', time, title)
    except IndexError:
        pass

def jinShan(number):
    print('\n\033[0;33m-----------------------金山 SRC------------------------\033[0m')
    url = 'https://security.wps.cn/api/src/notices?page=1&size=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['notices']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['content']
        title = notice_list[i]['title']
        print_color('金山',time,title)

def kuaiShou(number):
    print('\n\033[0;33m-----------------------快手 SRC------------------------\033[0m')
    url = 'https://security.kuaishou.com/api/user/notice/list?'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36',
        'Referer': 'https://security.kuaishou.com/notice'
    }
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['create_time']
        exp = time.rfind(" ")
        exp1 = time[exp:]
        time = time.replace(exp1,"")
        title = notice_list[i]['notice_title']
        print_color('快手',time,title)

def lsrc(number):
    print('\n\033[0;33m-----------------------联想 SRC------------------------\033[0m')
    url = 'https://lsrc.vulbox.com/news/?type=1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.news-list')[0].select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('.time')[0].text.strip() #匹配公告，第一条置顶公告，就是在notice_list盒子下的第四个li标签下的公告时间的div，并获取
        title = notice_list[i].select('a')[0].text
        print_color('联想', time, title)

def tClx(number):
    print('\n\033[0;33m-----------------------同程旅行 SRC------------------------\033[0m')
    url = 'https://sec.ly.com/index.php?m=&c=page&a=index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.announcement_list')[0].select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('.list_date')[0].text.strip() #匹配公告，第一条置顶公告，就是在notice_list盒子下的第四个li标签下的公告时间的div，并获取
        title = notice_list[i].select('a')[0].text
        print_color('同程旅行', time, title)

def mogu_src(number):
    print('\n\033[0;33m-----------------------美丽联合集团 SRC------------------------\033[0m')
    url = 'https://security.mogu.com/bulletin/list?pageNo=1&pageSize=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['result']['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['bulletinid']
        time = time[:-2]
        time01 = str(datetime.strptime(time, '%Y%m%d'))
        time01 = time01.replace('00:00:00','')
        title = notice_list[i]['bulletintitle']
        print_color('美丽联合', time01, title)

def meiZu(number):
    print('\n\033[0;33m-----------------------魅族 SRC------------------------\033[0m')
    url = 'https://sec.meizu.com/announcement/announcement_list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.col-md-12')[1].select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].text.strip().replace('【', '').replace('】', '').split(chr(160),maxsplit=1)[0]
        title = notice_list[i].select('a')[0].text
        print_color('魅族', time, title)

def buTian(number):
    print('\n\033[0;33m-----------------------补天 SRC------------------------\033[0m')
    url = 'https://www.butian.net/Article/lists?ajax=1&cid=&page=1&length=15'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time1 = notice_list[i]['create_time']
        time1 = int(time1)
        time1 = time.ctime(time1)
        time1 = datetime.strptime(time1, '%a %b  %d %H:%M:%S %Y')
        time1 = str(time1).split(" ", maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('补天', time1, title)

def sina(number):
    print('\n\033[0;33m-----------------------新浪 SRC------------------------\033[0m')
    url = 'https://sec.sina.com.cn/Announce/index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 14].select('.date')[0].text
        title = notice_list[i + 14].select('a')[0].text
        print_color('新浪', time, title)

def T3(number):
    print('\n\033[0;33m-----------------------T3出行安全 SRC------------------------\033[0m')
    url = 'https://security.t3go.cn/srcRefactor/notice/getNoticeList?type='
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['updateTime'].split(" ",maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('T3出行安全', time, title)

def wsrc(number):
    print('\n\033[0;33m-----------------------新浪微博 SRC------------------------\033[0m')
    url = 'https://wsrc.weibo.com/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 8].select('span')[0].text
        title = notice_list[i + 8].select('a')[0].text
        print_color('新浪微博', time, title)

def webank(number):
    print('\n\033[0;33m-----------------------微众银行 SRC------------------------\033[0m')
    url = 'https://security.webank.com/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 9].select('span')[0].text.replace("/","-")
        title = notice_list[i + 9].select('a')[0].text
        print_color('微众银行', time, title)

def wanMei(number):
    print('\n\033[0;33m-----------------------完美世界 SRC------------------------\033[0m')
    url = 'http://security.wanmei.com/board'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('li') #匹配到盒子里边的所有li标签
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.replace("/","-")
        title = notice_list[i].select('a')[0].text
        print_color('完美世界', time, title)

def wifi(number):
    print('\n\033[0;33m-----------------------wifi万能钥匙 SRC------------------------\033[0m')
    url = 'https://sec.wifi.com/api/announce'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publish_time'].split(" ", maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('wifi万能钥匙', time, title)

def xiaoMi(number):
    print('\n\033[0;33m-----------------------小米 SRC------------------------\033[0m')
    url = 'https://sec.xiaomi.com/api/v1/posts?pageNum=1&pageSize=10&categoryId=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime'].split(" ", maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('小米', time, title)

def xiaoYing(number):
    try:
        print('\n\033[0;33m-----------------------小赢 SRC------------------------\033[0m')
        url = 'https://security.xiaoying.com/index.php?m=&c=page&a=index'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'html.parser')
        notice_list = bs.select('li') #匹配到盒子里边的所有li标签
        if number > len(notice_list):
            number = len(notice_list)
        for i in range(0, number):
            time = notice_list[i + 6].select('span')[0].text.replace("/","-")
            title = notice_list[i + 6].select('a')[0].text
            print_color('小赢', time, title)
    except IndexError:
        pass

def xiMalaya(number):
    print('\n\033[0;33m-----------------------喜马拉雅 SRC------------------------\033[0m')
    url = 'https://security.ximalaya.com/announcement'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('.section-announcement')[0].select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.replace('/', '-')
        title = notice_list[i].select('a')[0].text
        print_color('喜马拉雅', time, title)

def ctrip(number):
    print('\n\033[0;33m-----------------------携程 SRC------------------------\033[0m')
    url = 'https://sec.ctrip.com/bulletin/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i].select('span')[0].text.replace('/', '-')
        title = notice_list[i].select('a')[0].text
        print_color('携程', time, title)

def wifi(number):
    print('\n\033[0;33m-----------------------wifi万能钥匙 SRC------------------------\033[0m')
    url = 'https://sec.wifi.com/api/announce'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publish_time'].split(" ", maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('wifi万能钥匙', time, title)

def xiaoMi(number):
    print('\n\033[0;33m-----------------------小米 SRC------------------------\033[0m')
    url = 'https://sec.xiaomi.com/api/v1/posts?pageNum=1&pageSize=10&categoryId=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['createTime'].split(" ", maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('小米', time, title)

def youZan(number):
    print('\n\033[0;33m-----------------------有赞 SRC------------------------\033[0m')
    url = 'https://src.youzan.com/index.php?m=&c=page&a=index'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 5].select('span')[0].text.replace('/', '-')
        title = notice_list[i + 5].select('a')[0].text
        print_color('有赞', time, title)

def unionpay(number):
    print('\n\033[0;33m-----------------------银联 SRC------------------------\033[0m')
    url = 'https://security.unionpay.com/notice/list?type=2'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    notice_list = bs.select('li')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i + 12].select('span')[0].text.replace('/', '-')
        title = notice_list[i + 12].select('a')[0].text.split(" ",maxsplit=1)[0]
        print_color('银联', time, title)

def creditease(number):
    print('\n\033[0;33m-----------------------宜信 SRC------------------------\033[0m')
    url = 'https://security.creditease.cn/api/web/announcement/queryList.json'
    headers = {
        'Host': 'security.creditease.cn',
        'Referer': 'https://security.creditease.cn/noticeList.html',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers,data='pageNum=1&pageSize=16',verify=False)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['releaseTime'].split(" ",maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('宜信', time, title)

def zhaopin(number):
    try:
        print('\n\033[0;33m-----------------------智联 SRC------------------------\033[0m')
        url = 'https://src.zhaopin.com/page'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'html.parser')
        notice_list = bs.select('li')
        if number > len(notice_list):
            number = len(notice_list)
        for i in range(0, number):
            time = notice_list[i + 10].select('span')[0].text.split(" ",maxsplit=1)[0]
            title = notice_list[i + 10].select('a')[0].text
            print_color('智联', time, title)
    except IndexError:
        pass

def zbj(number):
    try:
        print('\n\033[0;33m-----------------------猪八戒 SRC------------------------\033[0m')
        url = 'https://security.zbj.com/news/index.html'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'html.parser')
        notice_list = bs.select('a')
        if number > len(notice_list):
            number = len(notice_list)
        for i in range(0, number):
            if i == 1:
                continue
            time = notice_list[i + 9].select('p')[1].text.split(" ",maxsplit=1)[0]
            title = notice_list[i + 9].select('h1')[0].text
            print_color('猪八戒', time, title)
    except IndexError:
        pass

def ziroom(number):
    try:
        print('\n\033[0;33m-----------------------自如 SRC------------------------\033[0m')
        url = 'https://zrsecurity.ziroom.com/index.php?m=&c=page&a=index'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'html.parser')
        notice_list = bs.select('li')
        if number > len(notice_list):
            number = len(notice_list)
        for i in range(0, number):
            time = notice_list[i + 7].select('span')[0].text.replace("/","-")
            title = notice_list[i + 7].select('a')[0].text
            print_color('自如', time, title)
    except IndexError:
        pass

def intsig(number):
    try:
        print('\n\033[0;33m-----------------------合合 SRC------------------------\033[0m')
        url = 'https://security.intsig.com/index.php?m=&c=page&a=index'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
        r = requests.get(url, headers=headers)
        bs = BeautifulSoup(r.text, 'html.parser')
        notice_list = bs.select('li')
        if number > len(notice_list):
            number = len(notice_list)
        for i in range(0, number):
            time = notice_list[i + 8].select('span')[0].text.replace("/","-")
            title = notice_list[i + 8].select('a')[0].text
            print_color('合合', time, title)
    except IndexError:
        pass

def jj(number):
    print('\n\033[0;33m-----------------------竞技世界 SRC---------------------\033[0m')
    url = 'https://security.jj.cn/notice/notice_list1.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r = r.text.encode('iso-8859-1').decode('gbk')
    bs = BeautifulSoup(r, 'html.parser')
    notice_list = bs.select('td')
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number+1, 2):
          time = notice_list[i+1].text
          title = notice_list[i].text
          print_color('竞技世界', time, title)

def maFengwo(number):
    print('\n\033[0;33m-----------------------马蜂窝 SRC------------------------\033[0m')
    url = 'https://security.mafengwo.cn/api/article/list?limit=10&page=1&type=-1'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['list']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['create_time'].split(" ",maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('马蜂窝', time, title)

def douYu(number):
    print('\n\033[0;33m-----------------------斗鱼 SRC-----------------------\033[0m')
    url = 'https://security.douyu.com/api/v1/announcement_list?announcement_type=1&current=1&size=10'
    headers = {
        'Host': 'security.douyu.com',
        'Cookie': "session=10467af2-6872-4cad-abc0-c43fb9403b2e.ey0uuGaWrg-blOjq44KNbQq9lNg",
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-origin',
        'Cache-Control': 'max-age=0, no-cache',
        'Pragma': 'no-cache',
        'Te': 'trailers',
        'Connection':'keep-alive',
        'Referer': 'https://security.douyu.com'
    }
    r = requests.get(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['data']['records']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time = notice_list[i]['publish_time']
        title = notice_list[i]['title']
        print_color('斗鱼', time, title)

def iflytek(number):
    print('\n\033[0;33m-----------------------讯飞 SRC------------------------\033[0m')
    url = 'https://security.iflytek.com/index.php?m=&c=page&a=indexlist'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.post(url, headers=headers)
    r_json = json.loads(r.text)
    notice_list = r_json['result']
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
        time1 = notice_list[i]['update_time']
        time1 = int(time1)
        time1 = time.ctime(time1)
        time1 = datetime.strptime(time1, '%a %b  %d %H:%M:%S %Y')
        time1 = str(time1).split(" ", maxsplit=1)[0]
        title = notice_list[i]['title']
        print_color('讯飞', time1, title)

"""def tuYa(number):
    print('\n\033[0;33m-----------------------涂鸦 SRC---------------------\033[0m')
    url = 'https://src.tuyacn.com/announcement/list'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    r = requests.get(url, headers=headers)
    bs = BeautifulSoup(r.text, 'html.parser')
    print(bs)
    #notice_list = bs.select('.annouRow')
    print(notice_list)
    if number > len(notice_list):
        number = len(notice_list)
    for i in range(0, number):
          time = notice_list[i].text
          title = notice_list[i].text
          print_color('涂鸦', time, title)"""

if __name__ == '__main__':
    print('''\033[0;33m
   _____ ____  ______   _   __      __  _         
  / ___// __ \/ ____/  / | / /___  / /_(_)_______ 
  \__ \/ /_/ / /      /  |/ / __ \/ __/ / ___/ _ \\
 ___/ / _, _/ /___   / /|  / /_/ / /_/ / /__/  __/
/____/_/ |_|\____/  /_/ |_/\____/\__/_/\___/\___/ 

✔ 爬取各个SRC平台的公告通知
✔ 对2020年发布的活动通知进行红色高亮显示
✔ 将当天发布的公告推送到微信上，结合系统定时任务可实现SRC平台公告监测
✔ 支持的SRC平台[当前共计60家]

Version：0.3              date: 2022-05-04
Author_01: TeamsSix          微信公众号：TeamsSix	                Blog: teamssix.com            Github: github.com/teamssix
Author_02: 0dinary 	           QQ: 2996676785		wechat:C1994101Y	           Github: github.com/0dinary	
\033[0m''')
    global key
    key = 'SCT144100TzKQZ8Rz8Nvjv7UH9k6AHAiNm'  # 填写上你 Server酱的 key，key 申请地址：http://sc.ftqq.com/
    number = 4
    if key == '':
        print('请在代码第 1095 行填写上你 Server酱的 key，key 申请地址：http://sc.ftqq.com/')
        sys.exit()
    print('当前时间：%s' % time.strftime("%Y-%m-%d", time.localtime()))
    #tuYa(number)
    mogu_src(number)
    guaZi(number)
    jiaoDian(number)
    iflytek(number)
    maFengwo(number)
    jj(number)
    intsig(number)
    buTian(number)
    douYu(number)
    ziroom(number)
    zbj(number)
    zhaopin(number)
    creditease(number)
    unionpay(number)
    youZan(number)
    ctrip(number)
    xiMalaya(number)
    xiaoYing(number)
    xiaoMi(number)
    wifi(number)
    wanMei(number)
    webank(number)
    T3(number)
    sina(number)
    wsrc(number)
    meiZu(number)
    cainiao(number)  # 菜鸟裹裹
    tClx(number)
    lsrc(number)
    kuaiShou(number)
    dfcf(number)
    fuYou(number)
    huoLala(number)
    jinShan(number)
    boss(number)
    bigo(number)
    bytedance(number)  # 字节跳动
    jd(number)  # 京东
    pingan(number)  # 平安
    oppo(number)  # OPPO
    immomo(number)  # 陌陌
    alibaba(number)  # 阿里
    duxiaoman(number)  # 度小满
    src_360(number)  # 360
    src_58(number)  # 58
    iqiyi(number)  # 爱奇艺
    baidu(number)  # 百度
    ke(number)  # 贝壳
    bilibili(number)  # 哔哩哔哩
    didichuxing(number)  # 滴滴出行
    alipay(number)  # 蚂蚁金服
    meituan(number)  # 美团
    shuidihuzhu(number)  # 水滴互助
    sf_express(number)  # 顺丰
    tencent(number)  # 腾讯
    vivo(number)  # vivo
    src_163(number)  # 网易
    vip(number)  # 唯品会
    wifi(number)  # WIFI万能钥匙
    zto(number)  # 中通


