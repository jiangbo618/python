#!/usr/bin/evn python
# encoding: utf-8
# @version     : python 3.7
# @Time        :2020/3/3 11:37
# @Author      :Jiangbo Lin
# @Filename    :mail_attach.py 
# @Description :
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication


smtpport = 465  #或者587



if __name__ == '__main__':
    fromaddr = "xxx@qq.com"
    password = "xxxxxxx"
    toaddrs = ['xxx@qq.com']
    content = 'hello, this is email content.'
    textApart = MIMEText(content)
    imageFile = '1.png'
    imageApart = MIMEImage(open(imageFile, 'rb').read(), imageFile.split('.')[-1])
    imageApart.add_header('Content-Disposition', 'attachment', filename=imageFile)
    m = MIMEMultipart()
    m.attach(textApart)
    m.attach(imageApart)
    m['Subject'] = 'title'
    try:
        server = smtplib.SMTP('smtp.qq.com')
        server.login(fromaddr,password)
        server.sendmail(fromaddr, toaddrs, m.as_string())
        print('success')
        server.quit()
    except smtplib.SMTPException as e:            \
        print('error:',e) #打印错误
