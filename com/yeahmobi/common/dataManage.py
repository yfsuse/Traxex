#! /usr/bin/env python
# --*-- coding:utf-8 --*--

__author__ = 'jeff.yu'

import json
from com.yeahmobi.common.httpData import get_data


def list_to_json(httpdata):

    result, group = httpdata
    if isinstance(result, basestring):
        try:
            json_data = json.loads(result)
        except Exception as e:
            raise e
        else:
            pass
    elif isinstance(result, json):
        json_data = result
    else:
        pass

    key_index = len(group)
    try:
        struct_data = json_data.get('data').get('data')[1:]
    except AttributeError as e:
        raise e
    json_data = {}
    for data in struct_data:
        key = data[:key_index]
        value = data[key_index:]
        json_data[number_to_str(key)] = value
    return group, json_data


def data_arrange(mysql_data, druid_data):
    mysql, druid = mysql_data, druid_data
    group_data = mysql[0]
    mysql_data, druid_data = mysql[1:][0], druid[1:][0]
    if len(mysql_data) != len(druid_data):
        print 'group by {0} len(MySql Data) <> len(Druid Data)'
    else:
        keys = mysql_data.keys()
        for key in keys:
            print "{0}\t\t\t{1}".format(mysql_data.get(key), druid_data.get(key))


def number_to_str(seq):
    """
    :param seq: [1,2,3,4]
    :return: ['1', '2', '3', '4']
    """
    str_of_list = [str(data) for data in seq]
    return str(str_of_list)


if __name__ == '__main__':
    pass