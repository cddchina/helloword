#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="1131617381@qq.com"    #用户名
mail_pass=""   #口令 
 
 
sender = '1131617381@qq.com'
receivers = ['1131617381@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
message = MIMEText('Python mail send... this is a good job', 'plain', 'utf-8')
message['From'] = Header("Andy", 'utf-8')
message['To'] =  Header("ToAndy", 'utf-8')
 
subject = 'happy new year'
message['Subject'] = Header(subject, 'utf-8')
 
 
try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465) 
    #smtpObj.connect(mail_host, 465)    # 25 为 SMTP 端口号
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print "send OK"
except smtplib.SMTPException,e:
    print "Error: can not send,%s"%e
