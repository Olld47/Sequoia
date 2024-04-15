# -*- encoding: UTF-8 -*-

import logging
import settings
# from wxpusher import WxPusher
from util import barkPusher
from util import emailPusher
import datetime


def push(msg, title):
    if settings.config['push']['enable']:
        response = barkPusher.send_message(msg, title, key=settings.config['push']['bark_device_key'], group = 'stock')
        emailPusher.send_message(msg, title, sender=settings.config['push']['email_sender'], pwd= settings.config['push']['email_pwd'], receiver=settings.config['push']['email_receiver'])
    logging.info(msg)


def statistics(msg=None):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    # push(msg, date+' ETF数据提醒')
    logging.info(msg)


def strategy(msg=None):
    if msg is None or not msg:
        msg = '今日没有符合条件的股票'
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    push(msg, date +' 策略提醒')
