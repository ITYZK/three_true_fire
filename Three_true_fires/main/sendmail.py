#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def send_mail(data, receiver):
    '''
    函数功能：发送邮件
    函数参数: data为邮件内容，receiver为邮件接收方
    返回值：发送成功返回0，否则返回1
    '''
    mail_host = 'smtp.qq.com'
    port = 465
    send_by = "675248896@qq.com"
    password = 'gpmarcovgajsbcia'
    send_to = receiver

    message = MIMEText(data, 'plain', 'utf-8')
    message["From"] = Header(send_by)
    message["To"] = Header(send_to)
    message["Subject"] = Header('三味真火')
      
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, port)
        smtpObj.login(send_by, password) 
        smtpObj.sendmail(send_by, send_to, message.as_string())
        return 0
    except smtplib.SMTPException as e:
        print("无法发送邮件", e)
        return 1
    except Exception as e:
        print("发送失败", e)
        return 1

