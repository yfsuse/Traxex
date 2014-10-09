#! /usr/bin/env python
# coding = utf-8

__author__ = 'jeff.yu'


import urllib2
import urllib
from com.yeahmobi.common.errorCode import *
from com.yeahmobi.common.requestParser import RequestParser


def get_data(query_type,  query_data):
    query_data = query_data.replace(': ', ':').replace(', ', ',')
    group = RequestParser(query_data).get_group()
    if query_type == "mysql":
        query_url = "http://report.yeahmobi.com/report?"
    elif query_type == "druid":
        query_url = "http://resin-yeahmobi-214401877.us-east-1.elb.amazonaws.com:18080/report/report?"
    else: 
        exit(-1)
        print "{0}: query_type is invalid".format(QUERY_TYPE_INVALID)

    para_data = {"report_param":  query_data}
    post_data = urllib.urlencode(para_data)
    try:
        f = urllib2.build_opener().open(urllib2.Request(query_url, post_data), timeout=120)
    except Exception as e:
        print "{0}: can't get data [{1}]".format(HTTP_ERROR, e.message)
        exit(-1)
    content = f.read()
    return content, group


if __name__ == '__main__':
    # print get_data("mysql", '{"settings": {"time": {"start": 1399334400, "end": 1399420800, "timezone": 0}, "data_source": "ymds_druid_datasource", "pagination": {"size": 5000, "page": 0}}, "data": ["click", "conversion"], "group": ["hour", "offer_id"]}')
    print get_data("druid", '{"settings": {"time": {"start": 1411257600, "end": 1411344000, "timezone": 0}, "data_source": "ymds_druid_datasource", "report_id": "report-id12", "pagination": {"size":5000,"page":0}},"group":["hour"],"data":["click","conversion"],"filters":{"$and":{}},"sort":[]}')