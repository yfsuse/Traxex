#! /usr/bin/env python
# coding = utf-8

__author__ = 'jeff.yu'


from com.yeahmobi.common.sendMail import send_mail
from cases import Case
from com.yeahmobi.common.dateConv import get_range
from com.yeahmobi.common.dataManage import *


def main():

    case_list = Case().get_case()
    unix_start, unix_end = get_range()

    for case in case_list:
        case = case.replace("-1", unix_start).replace("-2", unix_end).replace(': ', ':').replace(', ', ',')
        print case
        # mysql_rsp = get_data("mysql", case)
        druid_rsp = get_data("druid", case)
        # mysql_data = list_to_json(mysql_rsp)
        druid_data = list_to_json(druid_rsp)
        # data_arrange(mysql_data, druid_data)
        print druid_data
        break

if __name__ == '__main__':
    main()