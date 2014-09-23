#! /usr/bin/env python
# coding = utf-8

__author__ = 'jeff.yu'


from com.yeahmobi.common.sendMail import send_mail
from com.yeahmobi.common.httpData import get_data
from com.yeahmobi.common.requestParser import RequestParser
from cases import Case
from com.yeahmobi.common.dateConv import get_range


def main():

    case_list = Case().get_case()
    unix_start, unix_end = get_range()

    for case in case_list:
        case = case.replace("-1", unix_start).replace("-2", unix_end)
        mysql_rsp = get_data("mysql", case)
        druid_rsp = get_data("druid", case)
        print mysql_rsp + '\n' +druid_rsp

if __name__ == '__main__':
    main()