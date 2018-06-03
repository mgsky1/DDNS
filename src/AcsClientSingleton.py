'''
@desc:AcsClient的单实例类
@author: Martin Huang
@time: created on 2018/5/26 18:50
@修改记录:
'''
from aliyunsdkcore.client import AcsClient
class AcsClientSing:
    __client = None

    @classmethod
    def getInstance(self):
        if self.__client is None:
            self.__client = AcsClient('Your_AccessKeyId', 'Your_AccessKeySecret', 'cn-hangzhou')
        return self.__client
