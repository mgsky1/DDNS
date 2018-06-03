'''
获取阿里云Common Request请求类
单实例
Created By Martin Huang on 2018/5/26
'''
from aliyunsdkcore.request import CommonRequest

class CommonRequestSing:
    #私有类变量
    __request = None

    #该修饰符将实例方法变成类方法
    #,因为类方法无法操作私有的类变量，所以使用实例方法进行操作，再进行转换为类方法
    @classmethod
    def getInstance(self):
        if self.__request is None:
            self.__request = CommonRequest()
        return self.__request

if __name__ == "__main__":
    CommonRequestSing.getInstance()
