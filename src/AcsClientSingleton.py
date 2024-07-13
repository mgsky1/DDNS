'''
@desc:AcsClient的单实例类
@author: Martin Huang
@time: created on 2018/5/26 18:50
@修改记录:
2018/6/10 =》 AccessKeyId 和 AccessKeySecret从配置文件中读取
2024/7/13 =》 避免循环导入
'''
from aliyunsdkcore.client import AcsClient
import json

class AcsClientSing:
    __client = None

    @classmethod
    def getInstance(self):
        if self.__client is None:
            with open('config.json') as file:
                acsDict = json.loads(file.read())
            self.__client = AcsClient(acsDict.get('AccessKeyId'), acsDict.get('AccessKeySecret'), 'cn-hangzhou')
        return self.__client
