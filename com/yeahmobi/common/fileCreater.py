__author__ = 'jeff.yu'


from com.yeahmobi.common.dataProducer import DataProducer
from json import dumps

def file_create(campaign_id, record_num = 100):

    record_list = []
    for index in range(record_num):
        dp = DataProducer(campaign_id)
        dp.set_click()
        dp.set_lp_click()
        dp.set_conversion()
        dp.set_others()
        record = {}
        record['time_stamp'] = dp.get_time_stamp()
        record['click_id'] = dp.get_click_id()
        record['campaign_id'] = dp.get_campaign_id()
        record['offer_id'] = dp.get_offer_id()
        record['ref_site'] = dp.get_ref_site()
        record['site'] = dp.get_site()
        record['click_time'] = dp.get_click_time()
        record['cost_per_click'] = dp.get_cost_per_click()
        record['payout'] = dp.get_payout()
        record['real_ip'] = dp.get_real_ip()
        record['proxy_ip'] = dp.get_proxy_ip()
        record['device_id'] = dp.get_device_id()
        record['os_id'] = dp.get_os_id()
        record['carrier_id'] = dp.get_carrier_id()
        record['mobile_brand_id'] = dp.get_mobile_brand_id()
        record['screen_h'] = dp.get_screen_h()
        record['screen_w'] = dp.get_screen_w()
        record['screen_id'] = dp.get_screen_id()
        record['city_id'] = dp.get_city_id()
        record['brand_id'] = dp.get_brand_id()
        record['model_id'] = dp.get_model_id()
        record['country_id'] = dp.get_country_id()
        record['state_id'] = dp.get_state_id()
        record['conversion_time'] = dp.get_conversion_time()
        record['event'] = dp.get_event()
        record['sub1'] = dp.get_sub1()
        record['sub2'] = dp.get_sub2()
        record['sub3'] = dp.get_sub3()
        record['sub4'] = dp.get_sub4()
        record['sub5'] = dp.get_sub5()
        record['sub6'] = dp.get_sub6()
        record['sub7'] = dp.get_sub7()
        record['sub8'] = dp.get_sub8()
        record['click'] = dp.get_click()
        record['lp_click'] = dp.get_lp_click()
        record['conversion'] = dp.get_conversion()
        record_str = dumps(record).replace("'", '"')
        record_list.append(record_str)

        with open('../output/trading_desk.json', 'w') as f:
            for line in record_list:
                f.writelines(line + '\n')


if __name__ == '__main__':
    file_create(100)