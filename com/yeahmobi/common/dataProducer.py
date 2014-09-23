#! /usr/bin/env python
# coding = utf-8

__author__ = 'jeff.yu'

from random import choice
from string import lowercase
from string import digits


"""
{"time_stamp":"2014-01-02T01:10:00Z",
"click_id":"43306130-ff65-436b-9851-1e2650000021",
"campaign_id":"t_571",
"offer_id":109,
"ref_site":"",
"site":"",
"click_time":"2014-01-02T01:10:00Z",
"cost_per_click":10.264,
"payout":4.491,
"real_ip":"147.12.35.1",
"proxy_ip":"172.30.14.11",
"device_id":18,
"os_id":149,
"carrier_id":1,
"mobile_brand_id":3,
"screen_h":6,
"screen_w":8,
"screen_id":7,
"city_id":2,
"brand_id":1,
"model_id":4,
"country_id":3,
"state_id":4,
"conversion_time":"2014-01-02T01:10:00Z",
"event":1,
"sub1":"night",
"sub2":"",
"sub3":"",
"sub4":"",
"sub5":"",
"sub6":"",
"sub7":"",
"sub8":"",
"click":0,
"lp_click":0,
"conversion":1}
"""


def n_choice(seq, num):
    seq = lowercase + digits
    result = ''
    for i in range(num):
        result += choice(seq)
    return result


class DataProducer(object):

    def __init__(self, campaign_id):
        self.timestamp = ''
        self.campaign_id = campaign_id
        self.click_id = ''
        self.offer_id = ''
        self.ref_site = ''
        self.site = ''
        self.click_time = ''
        self.cost_per_click = ''
        self.payout = ''
        self.real_ip = ''
        self.proxy_ip = ''
        self.device_id = ''
        self.os_id = ''
        self.carrier_id = ''
        self.screen_id = ''
        self.screen_h = ''
        self.screen_w = ''
        self.mobile_brand_id = ''
        self.model_id = ''
        self.brand_id = ''
        self.country_id = ''
        self.city_id = ''
        self.state_id = ''
        self.conversion_time = ''
        self.event = ''
        self.sub1 = ''
        self.sub2 = ''
        self.sub3 = ''
        self.sub4 = ''
        self.sub5 = ''
        self.sub6 = ''
        self.sub7 = ''
        self.sub8 = ''
        self.click = ''
        self.lp_click = ''
        self.conversion = ''

    def get_data(self):
        pass

    def set_timestamp(self):
        """
        :return:2014-01-02T01:10:00Z

        """
        year = choice((2013, 2014))
        month = choice(range(1, 12))
        day = choice(range(1, 29))
        hour = choice(range(0, 24))
        minute = choice(range(0, 60))
        second = choice(range(0, 60))

        self.timestamp = "{0}-{1}-{2}T{3}:{4}:{5}Z".format(year, month, day, hour, minute, second)

    def get_time_stamp(self):
        return self.timestamp

    def set_click_id(self):
        self.click_id = "{0}-{1}-{2}-{3}-{4}".format(n_choice(8), n_choice(4),
                                                     n_choice(4), n_choice(4),
                                                     n_choice(12))

    def get_click_id(self):
        return self.click_id

    def get_campaign_id(self):
        return self.campaign_id

    def set_offer_id(self):
        if self.lp_click == 1:
            self.offer_id = -1
        else:
            self.offer_id = choice(('2205', '2206', '2207', '2208', '2209'))

    def get_offer_id(self):
        return self.offer_id

    def set_ref_site(self):
        self.ref_site = choice(('http://www.oracle.com', 'http://www.google.com', 'http://www.taobao.com',
                                'http://www.apple.com', 'http://www.yahoo.com', 'http://www.alibaba.com'))

    def get_ref_site(self):
        return self.ref_site

    def set_site(self):
        self.site = self.get_ref_site().split("//")[1]

    def get_site(self):
        return self.site

    def set_click_time(self):
        self.click_time = self.timestamp

    def get_click_time(self):
        return self.click_time

    def set_cost_per_click(self):
        self.cost_per_click = choice((10.27, 12.23, 22.33, 9.22, 9.88, 14.43))

    def get_cost_per_click(self):
        return self.cost_per_click

    def set_payout(self):
        self.payout = choice((10.27, 12.23, 22.33, 9.22, 9.88, 14.43))

    def get_payout(self):
        return self.payout

    def set_real_ip(self):
        self.real_ip = choice(('43.32.189.23', '123.98.88.12', '10.1.15.44',
                               '12.99.33.121', '10.1.5.99', '79.50.32.11'))

    def get_real_ip(self):
        return self.real_ip

    def set_proxy_ip(self):
        self.proxy_ip = choice(('43.32.189.23', '123.98.88.12', '10.1.15.44',
                               '12.99.33.121', '10.1.5.99', '79.50.32.11'))

    def get_proxy_ip(self):
        return self.proxy_ip

    def set_device_id(self):
        self.device_id = choice((1, 2, 3))

    def get_device_id(self):
        return self.device_id

    def set_os_id(self):
        self.os_id = choice((1, 2, 3))

    def get_os_id(self):
        return self.os_id

    def set_carrier_id(self):
        self.carrier_id = choice((1, 2, 3, 4))

    def get_carrier_id(self):
        return self.campaign_id

    def set_mobile_brand_id(self):
        self.mobile_brand_id = choice((1, 2, 3, 4))

    def get_mobile_brand_id(self):
        return self.mobile_brand_id

    def set_screen_h(self):
        self.screen_h = choice((1280, 960, 480, 320))

    def get_screen_h(self):
        return self.screen_h

    def set_screen_w(self):
        self.screen_w = choice((1280, 960, 480, 320))

    def get_screen_w(self):
        return self.screen_w

    def set_screen_id(self):
        self.screen_id = choice((1, 2, 3, 4))

    def get_screen_id(self):
        return self.screen_id

    def set_city_id(self):
        self.city_id = choice(range(1, 50))

    def get_city_id(self):
        return self.city_id

    def set_brand_id(self):
        self.brand_id = choice(range(1, 50))

    def get_brand_id(self):
        return self.brand_id

    def set_model_id(self):
        self.model_id= choice(range(1, 50))

    def get_model_id(self):
        return self.model_id

    def set_country_id(self):
        self.country_id= choice(range(1, 50))

    def get_country_id(self):
        return self.country_id

    def set_state_id(self):
        self.state_id= choice(range(1, 50))

    def get_state_id(self):
        return self.state_id

    def set_conversion_time(self):
        if self.conversion == 1:
            self.conversion_time = self.timestamp
        else:
            self.click = 1

    def get_conversion_time(self):
        return self.conversion_time

    def set_event(self):
        self.event= choice(range(1, 50))

    def get_event(self):
        return self.event

    def set_sub1(self):
        self.sub1 = "sub1_" + n_choice(4)

    def get_sub1(self):
        return self.sub1

    def set_sub2(self):
        self.sub2 = "sub2_" + n_choice(4)

    def get_sub2(self):
        return self.sub2

    def set_sub3(self):
        self.sub3 = "sub3_" + n_choice(4)

    def get_sub3(self):
        return self.sub3

    def set_sub4(self):
        self.sub4 = "sub4_" + n_choice(4)

    def get_sub4(self):
        return self.sub4

    def set_sub5(self):
        self.sub5 = "sub5_" + n_choice(4)

    def get_sub5(self):
        return self.sub5

    def set_sub6(self):
        self.sub6 = "sub6_" + n_choice(4)

    def get_sub6(self):
        return self.sub6

    def set_sub7(self):
        self.sub7 = "sub7_" + n_choice(4)

    def get_sub7(self):
        return self.sub7

    def set_sub8(self):
        self.sub8 = "sub8_" + n_choice(4)

    def get_sub8(self):
        return self.sub8

    def set_click(self):
        self.click = choice((0, 1))

    def get_click(self):
        return self.click

    def set_lp_click(self):
        self.lp_click = choice((0, 1))

    def get_lp_click(self):
        return self.lp_click

    def set_conversion(self):
        self.conversion = choice((0, 1))

    def get_conversion(self):
        return self.conversion

    def set_others(self):
        self.set_timestamp()
        self.set_click_id()
        self.set_offer_id()
        self.set_brand_id()
        self.set_carrier_id()
        self.set_city_id()
        self.set_click_time()
        self.set_conversion_time()
        self.set_cost_per_click()
        self.set_country_id()
        self.set_device_id()
        self.set_device_id()
        self.set_screen_h()
        self.set_screen_id()
        self.set_screen_w()
        self.set_ref_site()
        self.set_state_id()
        self.set_site()
        self.set_sub1()
        self.set_sub2()
        self.set_sub3()
        self.set_sub4()
        self.set_sub5()
        self.set_sub6()
        self.set_sub7()
        self.set_sub8()
        self.set_proxy_ip()
        self.set_payout()
        self.set_os_id()
        self.set_mobile_brand_id()
        self.set_model_id()

