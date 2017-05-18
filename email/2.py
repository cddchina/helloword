# -*- coding: UTF-8 -*-
import smtplib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


def send_email(from_addr, to_addr, subject, password):
    msg = MIMEText("邮件正文",'html','utf-8')
    msg['From'] = u'<%s>' % from_addr
    msg['To'] = u'<%s>' % to_addr
    msg['Subject'] = subject

    smtp = smtplib.SMTP_SSL('smtp.qq.com', 587)
    smtp.set_debuglevel(1)
    smtp.ehlo("smtp.qq.com")
    smtp.login(from_addr, password)
    smtp.sendmail(from_addr, [to_addr], msg.as_string())


if __name__ == "__main__":
    # 这里的密码是开启smtp服务时输入的客户端登录授权码，并不是邮箱密码
    # 现在很多邮箱都需要先开启smtp才能这样发送邮件
    send_email(u"1131617381@qq.com",u"1131617381@qq.com",u"主题test",u"")
