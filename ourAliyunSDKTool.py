#!/usr/bin/env python3
# encoding: utf-8


'''
@desc:AcsClient的单实例类
@author: Martin Huang
'''

from aliyunsdkcore.client import AcsClient


class AcsClientSing:
    __client = None

    def __init__(self):
        pass

    @classmethod
    def getInstance(cls, accessKeyId, accessKeySecret, region):
        if cls.__client is None:
            cls.__client = AcsClient(accessKeyId, accessKeySecret, region)
        return cls.__client


'''
获取阿里云Common Request请求类单实例
Created By Martin Huang on 2018/5/26
'''
from aliyunsdkcore.request import CommonRequest


class CommonRequestSing:
    #私有类变量
    __request = None

    def __init__(self):
        pass

    #该修饰符将实例方法变成类方法
    #,因为类方法无法操作私有的类变量，所以使用实例方法进行操作，再进行转换为类方法
    @classmethod
    def getInstance(cls):
        if cls.__request is None:
            cls.__request = CommonRequest()
        return cls.__request