#! /usr/bin/env python
# coding = utf-8

__author__ = 'jeff.yu'


import json
import urllib2
import urllib


def get_data(query_type,  query_data): 

    if query_type == "mysql":
        query_url = "http://report.yeahmobi.com/report?"
    elif query_type == "druid":
        query_url = "http://resin-yeahmobi-214401877.us-east-1.elb.amazonaws.com:18080/report/report?"
    else: 
        exit(-1)
        print "query_type is invalid"
    print query_data
    para_data = {"report_param":  query_data}
    post_data = urllib.urlencode(para_data)
    try:
        f = urllib2.build_opener().open(urllib2.Request(query_url, post_data))
    except urllib2.HTTPError as e:
        print "Urllib2 HttpError : " + e.msg
        exit(-1)
    content = f.read()
    return content

if __name__ == '__main__': 
    print get_data("mysql", '{"settings": {"time": {"start": 1399334400, "end": 1399420800, "timezone": 0}, "data_source": "ymds_druid_datasource", "pagination": {"size": 50, "page": 0}}, "data": ["click", "conversion"], "group": ["hour", "offer_id"]}')
    print get_data("druid",  '{"settings": {"time": {"start": 1411257600, "end": 1411344000, "timezone": 0}, "data_source": "ymds_druid_datasource", "report_id": "report-id", "pagination": {"size":50,"page":0}},"group":["hour"],"data":["click","conversion"],"filters":{"$and":{}},"sort":[]}')