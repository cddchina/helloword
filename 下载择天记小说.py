#! /usr/lib/python
#-*- coding:GBK -*-
import time
import sys
import urllib
import http.cookiejar
import os
import re
import importlib
from bs4 import BeautifulSoup

url1 = 'http://www.xxbiquge.com' #/5_5422/1068292
# import js2html
class renrenSpider:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.id = ''
        self.sid = ''
        try:
            self.cookie =  http.cookiejar.CookieJar() #cookielib.CookieJar()
            self.cookieProc = urllib.request.HTTPCookieProcessor(self.cookie)
        except:
            raise
        else:
            opener = urllib.request.build_opener(self.cookieProc)
            opener.addheaders = [
                ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:53.0) Gecko/20100101 Firefox/53.0')]
            urllib.request.install_opener(opener)

    def login(self):
        url = 'http://www.xxbiquge.com/5_5422/'  #
        postdata = {
            'tbUserName': self.email,
            'tbPassword': self.password,
            'btnLogin': '确定',
            '__VIEWSTATE': '/wEPDwUJNDIzOTY1MjU5DxYEHg5NdXN0Q2hlY2tSaWdodGgeClBhZ2VVc2VySURlFgICAQ9kFgICBQ8PZBYCHgxBVVRPQ09NUExFVEUFA29mZmRkV1Hchudp6r72LgVP7TF2g2n4bIY=',
            '__VIEWSTATEGENERATOR': 'E19C8057',
            '__EVENTVALIDATION': '/wEWBAL0lobSBQLyj/OQAgK3jsrkBAKC3IeGDJ3I940/BYOzBiTkvwJ6gin0bVfU'
        }

        req = urllib.request.Request(url) #urllib.parse.urlencode(postdata)
        index = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(index, 'html.parser')
        temp = soup.findAll('a', attrs={'href': re.compile('^/5_5422/')})

        path_out = 'G:\\ztj.txt'
        f_out = open(path_out, 'w')

        for i in range(temp.__len__()):
            str = temp[i].decode()
            strUrl = re.findall(r"^<a href=\"(.+)\.html\">",str)
            strName = re.findall(r">(.+)<", str)
            print(strUrl)
            if strUrl.__len__() < 1:
                continue
            text = url1+ strUrl[0] +'.html'
            req2 = urllib.request.Request(text)
            index = urllib.request.urlopen(req2).read()
            soup = BeautifulSoup(index, 'html.parser')
            temp2 = soup.findAll('div', attrs={'id': re.compile('content')})
            #temp2 = temp2.decode()
            f_out.write('[**%s**]\r\n' % strName[0])
            for j in range(temp2.__len__()):
                string = temp2[j].decode()
                string = string.replace(u'\xa0', u' ') #\ufeff
                string = string.replace(u'\ufeff', u' ') #\ue13e
                string = string.replace(u'\ue13e', u' ') # \ue23a
                string = string.replace(u'\ue23a', u' ')
                try:
                    f_out.write(string)
                except Exception as e:
                    print ('Erroe:%s' % e)
                    continue
            print ('i=%d\n' % i)
            #if i > 10:
            #   break
        f_out.close()


if __name__ == '__main__':
    email = '2984'  # raw_input("输入人人网账号")
    password = 'Zxc111111'  # raw_input("输入人人网密码")
    #importlib.reload(sys)
    #sys.setdefaultencoding('utf-8') python2 is invaild
    renrenLogin = renrenSpider(email, password)
    renrenLogin.login()