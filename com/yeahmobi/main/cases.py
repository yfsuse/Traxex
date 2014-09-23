__author__ = 'jeff.yu'

import json


class Case(object):

    GROUP_BY_H = {"settings": {"time": {"start": int("-1"), "end": int("-2"), "timezone": 0}, "report_id": "cddcjio239c", "data_source": "ymds_druid_datasource", "pagination": {"size": 10000, "page": 0}}, "data": ["click", "conversion"], "group": ["hour"]}
    GROUP_BY_A_O = {"settings": {"time": {"start": -1, "end": -2, "timezone": 0}, "report_id": "cddcjio239c", "data_source": "ymds_druid_datasource", "pagination": {"size": 10000, "page": 0}}, "data": ["click", "conversion"], "group": ["aff_id", "offer_id"]}
    GROUP_BY_A = {"settings": {"time": {"start": -1, "end": -2, "timezone": 0}, "report_id": "cddcjio239c", "data_source": "ymds_druid_datasource", "pagination": {"size": 10000, "page": 0}}, "data": ["click", "conversion"], "group": ["aff_id"]}
    GROUP_BY_A_A_O = {"settings": {"time": {"start": -1, "end": -2, "timezone": 0}, "report_id": "cddcjio239c", "data_source": "ymds_druid_datasource", "pagination": {"size": 10000, "page": 0}}, "data": ["click", "conversion"], "group": ["aff_manager", "aff_id", "offer_id"]}
    GROUP_BY_O_H = {"settings": {"time": {"start": -1, "end": -2, "timezone": 0}, "report_id": "cddcjio239c", "data_source": "ymds_druid_datasource", "pagination": {"size": 10000, "page": 0}}, "data": ["click", "conversion"], "group": ["offer_id", "hour"]}
    GROUP_BY_A = {"settings": {"time": {"start": -1, "end": -2, "timezone": 0}, "report_id": "cddcjio239c", "data_source": "ymds_druid_datasource", "pagination": {"size": 10000, "page": 0}}, "data": ["click", "conversion"], "group": ["aff_manager"]}
    GROUP_BY_A_O = {"settings": {"time": {"start": -1, "end": -2, "timezone": 0}, "report_id": "cddcjio239c", "data_source": "ymds_druid_datasource", "pagination": {"size": 10000, "page": 0}}, "data": ["click", "conversion"], "group": ["advertiser_id", "offer_id"]}

    def __init__(self):
        pass

    def get_case(self):
        case_map = []
        class_dict = self.__class__.__dict__
        for key in class_dict:
            if key.startswith('GROUP'):
                case_map.append(class_dict[key])
        return [json.dumps(case) for case in case_map]


if __name__ == '__main__':
    print Case().get_case()