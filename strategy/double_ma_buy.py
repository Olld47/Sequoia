# -*- encoding: UTF-8 -*-

import talib as tl
import pandas as pd
import logging
from datetime import datetime, timedelta

# 双均线买入
def check(code_name, data, end_date=None, threshold=30):
    if len(data) < threshold:
        logging.debug("{0}:样本小于{1}天...\n".format(code_name, threshold))
        return
    data['ma5'] = pd.Series(tl.MA(data['收盘'].values, 5), index=data.index.values)
    data['ma20'] = pd.Series(tl.MA(data['收盘'].values, 20), index=data.index.values)

    if end_date is not None:
        mask = (data['日期'] <= end_date)
        data = data.loc[mask]

    data = data.tail(n=threshold)

    # step1 = round(threshold/3)
    # step2 = round(threshold*2/3)
        
    if data['ma20'].iloc[-1] < data['ma5'].iloc[-1] and \
        data['ma5'].iloc[-2] < data['ma20'].iloc[-2]:
        return True
    else:
        return False

