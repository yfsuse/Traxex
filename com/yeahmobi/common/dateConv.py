__author__ = 'jeff.yu'

# -*- coding: utf-8 -*-

import time
import datetime


def get_range():
    currentDate = datetime.date.today() + datetime.timedelta(hours=8)
    lastDate = (currentDate - datetime.timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')
    currentDate = currentDate.strftime('%Y-%m-%d %H:%M:%S')
    unix_start, unix_end = datetime_timestamp(lastDate), datetime_timestamp(currentDate)
    return unix_start, unix_end

def timestamp_datetime(value):
    format = '%Y-%m-%d %H:%M:%S'
    value = time.localtime(value)
    dt = time.strftime(format, value)
    return dt


def datetime_timestamp(dt):
    s = time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
    return str(int(s))

if __name__ == '__main__':
    print get_range()


