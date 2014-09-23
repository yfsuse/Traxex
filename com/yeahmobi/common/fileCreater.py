__author__ = 'jeff.yu'


from com.yeahmobi.common.dataProducer import DataProducer

def file_create(campaign_id, record_num = 100):

    dp = DataProducer(campaign_id)
    dp.set_click()
    dp.set_lp_click()
    dp.set_conversion()
    dp.set_others()

if __name__ == '__main__':
    file_create(100)