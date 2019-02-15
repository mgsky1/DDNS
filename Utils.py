#!/usr/bin/env python3
# encoding: utf-8


import requests
import json
import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)


from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.acs_exception.exceptions import ClientException


from ourAliyunSDKTool import AcsClientSing, CommonRequestSing


class Utils:

    def __init__(self):
        pass


    #获取真实公网IP
    @staticmethod
    def getRealIp():
        try:
            s = requests.get('https://ident.me/.json')
            info = json.loads(s.content.decode(encoding="utf-8"))
            ip = info["address"]
        except Exception as e:
            ip = None
        return ip

    #获取二级域名的RecordId
    @staticmethod
    def getRecordId(client, request, firstDomain, secondDomain):
        recordIds = {}
        request.set_domain('alidns.aliyuncs.com')
        request.set_version('2015-01-09')
        request.set_action_name('DescribeDomainRecords')
        request.add_query_param('DomainName', firstDomain)
        response = client.do_action_with_exception(request)
        jsonObj = json.loads(response.decode("UTF-8"))
        records = jsonObj["DomainRecords"]["Record"]
        for each in records:
            if each["RR"] in secondDomain:
                recordIds[each["RR"]] = each["RecordId"]
        return recordIds


    #从json中获取信息JSON串
    @staticmethod
    def getJson(path):
        jsonStr = {}
        with open(path, 'r') as file:
            jsonStr = json.load(file)
        return jsonStr


    @staticmethod
    def setJson(path, data):
        with open(path, 'w') as f:
            json.dump(data, f)


    @staticmethod
    def DDNS(configJSON, ip):
        response = True
        config = Utils.getJson(configJSON)

        client = AcsClientSing.getInstance(config.get('accessKeyId'), config.get('accessKeySecret'), config.get('region'))
        request = CommonRequestSing.getInstance()

        recordIds = Utils.getRecordId(client, request, config.get('first-level-domain'), config.get('second-level-domain'))

        logger.info('recordIds: %s'%recordIds)
        for secondDomain, recordId in recordIds.items():
            try:
                request.set_domain('alidns.aliyuncs.com')
                request.set_version('2015-01-09')
                request.set_action_name('UpdateDomainRecord')
                request.add_query_param('RecordId', recordId)
                request.add_query_param('RR', secondDomain)
                request.add_query_param('Type', 'A')
                request.add_query_param('Value', ip)
                response = client.do_action_with_exception(request)
                logger.info("success %s"%response)
            except (ServerException, ClientException) as reason:
                logger.warn("fail %s"%reason.get_error_msg())
                response = False
        return response

