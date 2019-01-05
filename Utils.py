'''
工具类
Created By Martin Huang on 2018/5/19
修改记录：
2018/5/16 =》删除不需要的方法
2018/5/29 =》增加获取操作系统平台方法，增加网络连通性检测(后续考虑重构)
2018/6/3 =》网络连通性代码重构
2018/6/10 =》增加配置文件读取方法(可能有IO性能影响，考虑重构)
'''


import requests
import json


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
            s = requests.get('https://api.ipify.org/?format=json')
            info = json.loads(s.content.decode(encoding="utf-8"))
            ip = info["ip"]
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

        print('recordIds', recordIds)
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
                print("success", response)
            except (ServerException, ClientException) as reason:
                print("fail", reason.get_error_msg())
                response = False
        return response

