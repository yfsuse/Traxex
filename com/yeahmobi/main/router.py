#! /usr/bin/env python
# --*-- coding:utf-8 --*--
__author__ = 'jeff.yu'


from random import choice
import sys
import os


class Router(object):

    def __init__(self):
        self.getDataFromBroker()

    def getBrokerIp(self):
        return choice(('10.1.5.30', '10.1.5.31'))

    def getDataFromBroker(self):
        brokerIp = self.getBrokerIp()
        requestBody = self.getJsonBody()
        self.dataReceived = []
        for requestFile in requestBody:
            sendBody = "curl -X post http://{0}:8080/druid/v2/?pretty -H 'content-type: application/json' -d @{1}".format(brokerIp, requestFile)
            print sendBody
            data = os.popen(sendBody).read()
            print data
            self.dataReceived.append(data)

    def getJsonBody(self):
        absPath = sys.path[0].replace('main', 'tableRouter/')
        jsonFile = os.listdir(absPath)
        return [absPath + f for f in jsonFile if f.startswith('table')]

    @property
    def check(self):
        if len(self.dataReceived) == len(set(self.dataReceived)):
            return True
        else:
            return False

if __name__ == '__main__':
    router = Router()
    print router.check