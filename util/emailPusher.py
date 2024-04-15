import smtplib
import logging
from email.mime.text import MIMEText


def send_message(content, title, **kwargs):

    # 设置发件人和收件人
    sender = kwargs.get('sender') 
    receiver = kwargs.get('receiver')
    pwd = kwargs.get('pwd')
    # 设置邮件主题和正文
    subject = title
    body = content

    # 创建邮件对象
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    # 发送邮件
    with smtplib.SMTP('smtp.163.com') as smtp:
        smtp.starttls()  # 启用安全传输层协议
        smtp.login(sender, pwd)  # 登录邮箱
        smtp.send_message(msg)
        logging.info(f'msg: {msg}, Email sent successfully!')