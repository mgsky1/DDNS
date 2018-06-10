'''
@desc:AcsClient的单实例类
@author: Martin Huang
@time: created on 2018/5/26 18:50
@修改记录:
2018/6/10 =》 AccessKeyId 和 AccessKeySecret从配置文件中读取
'''
from aliyunsdkcore.client import AcsClient
import Utils as tools
class AcsClientSing:
    __client = None

    @classmethod
    def getInstance(self):
        if self.__client is None:
            acsDict = tools.Utils.getConfigJson()
            self.__client = AcsClient(acsDict.get('AccessKeyId'), acsDict.get('AccessKeySecret'), 'cn-hangzhou')
        return self.__client
