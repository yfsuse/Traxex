__author__ = 'jeff.yu'


import json


class RequestParser(object):

    def __init__(self, request):
        self.request = request
        self.json_object = self.set_object()

    def set_object(self):
        object_json = self.request
        try:
            object_json = json.loads(self.request)
        except TypeError as e:
            pass

        return object_json

    def get_group(self):
        return self.set_object().get('group')

    def get_data(self):
        return self.set_object().get('data')

    def get_dimensions(self):
        return self.get_data() + self.get_group()


if __name__ == '__main__':
    rp = RequestParser({"settings": {"time": {"start": 1399334400, "end": 1399420800, "timezone": 0}, "data_source": "ymds_druid_datasource", "pagination": {"size": 50, "page": 0}}, "data": ["click", "conversion"], "group": ["hour", "offer_id"]})
    print rp.get_dimensions()
