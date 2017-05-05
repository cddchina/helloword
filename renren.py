#! /usr/bin/env python
#coding:utf-8
 
import sys
import re
import urllib2
import urllib
import requests
import cookielib
 
## Õâ¶ÎŽúÂëÊÇÓÃÓÚœâŸöÖÐÎÄ±šŽíµÄÎÊÌâ  
reload(sys)  
sys.setdefaultencoding("utf8")  
#####################################################
#µÇÂŒÈËÈË
#loginurl = 'http://www.renren.com/PLogin.do'  'domain':self.domain,
loginurl = 'http://oa-center/Programs/login/login.aspx'
logindomain = '确定'
 
KQurl = 'http://oa-center/Programs/KQ/EmployeeInfoStatistic.aspx'
class Login(object):
     
    def __init__(self):
        self.name = ''
        self.passwprd = ''
        self.domain = ''
 
        self.cj = cookielib.LWPCookieJar()            
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj)) 
        urllib2.install_opener(self.opener)    
     
    def setLoginInfo(self,username,password,domain):
        '''设置用户登录信息'''
        self.name = username
        self.pwd = password
        self.domain = domain
 
    def login(self):
        '''登录网站'''
        loginparams = {'tbUserName':self.name, 'tbPassword':self.pwd,'btnLogin':self.domain,'__VIEWSTATE':'/wEPDwUJNDIzOTY1MjU5DxYEHg5NdXN0Q2hlY2tSaWdodGgeClBhZ2VVc2VySURlFgICAQ9kFgICBQ8PZBYCHgxBVVRPQ09NUExFVEUFA29mZmRkV1Hchudp6r72LgVP7TF2g2n4bIY=','__VIEWSTATEGENERATOR':'E19C8057','__EVENTVALIDATION':'/wEWBAL0lobSBQLyj/OQAgK3jsrkBAKC3IeGDJ3I940/BYOzBiTkvwJ6gin0bVfU'}
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0'}
        req = urllib2.Request(loginurl, urllib.urlencode(loginparams),headers=headers)  
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
	print thePage
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0','Cookie':'ASP.NET_SessionId=1ct1sk55v2sbsy450auwjuat','Referer':'http://oa-center/Programs/KQ/EmployeeInfoStatistic.aspx'}
        loginparams = {'TimeSelect':'RadioButtonPREV_MONTH','btnSearch':'查询'}
        req = urllib2.Request(KQurl, urllib.urlencode(loginparams),headers=headers)  
        response = urllib2.urlopen(req)
        self.operate = self.opener.open(req)
        thePage = response.read()
	print thePage


       
         
if __name__ == '__main__':   
    userlogin = Login()
    username = '2984'
    password = 'Zxc111111'
    domain = logindomain
    userlogin.setLoginInfo(username,password,domain)
    userlogin.login()
