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


# import js2html
class renrenSpider:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.domain = 'renren.com'
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
        url = 'http://www.renren.com/PLogin.do'  #
        postdata = {
            'email': self.email,
            'password': self.password,
            'domain': self.domain
        }
        req = urllib.request.Request(url, urllib.parse.urlencode(postdata).encode(encoding='UTF8'))
        index = urllib.request.urlopen(req).read()
        #soup = BeautifulSoup(index, 'html.parser')
        print (index)

        postdata1 = {
            'channel': 'renren',
            'content': '人生苦短 我用Python',
            'withInfo': 'xxxxxxxxx',
            'privacyParams': 'xxxxxxxxx',
            'requestToken': 'xxxxxxxx',
            '_rtk': 'xxxxxx'
        }

        nextPageUrl = 'http://shell.renren.com/422393371/status'
        req = urllib.request.Request(nextPageUrl, urllib.parse.urlencode(postdata1).encode(encoding='UTF8'))
        statusFile = urllib.request.urlopen(req).read()
        print (statusFile)


if __name__ == '__main__':
    email = 'xxxxx'  # raw_input("输入人人网账号")
    password = 'xxxx'  # raw_input("输入人人网密码")
    #importlib.reload(sys)
    #sys.setdefaultencoding('utf-8') python2 is invaild
    renrenLogin = renrenSpider(email, password)
    renrenLogin.login()  