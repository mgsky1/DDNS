'''
DDNS 主程序 使用阿里云的SDK发起请求
Created By Martin Huang on 2018/5/20
修改记录：
2018/5/20 => 第一版本
2018/5/26 => 增加异常处理、Requst使用单例模式，略有优化
2018/5/29 => 增加网络连通性检测，只有联通时才进行操作，否则等待
2018/6/10 => 使用配置文件存储配置，避免代码内部修改(需要注意Python模块相互引用问题)
2018/9/24 => 修改失败提示信息
2018/12/27 => 增加参数-6，用于更新ipv6的记录 感谢@Li Kaiwei
2019/4/13 => 更新功能，支持多个二级域名映射 感谢@lsl061085的建议
'''
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.acs_exception.exceptions import ClientException
from Utils import Utils
import time
import argparse

def DDNS(use_v6):
    client = Utils.getAcsClient()
    domains = Utils.getConfigJson().get('Second-level-domain').split(',');
    drDict = Utils.getRecordIdAndDomainsDict(domains)
    print(drDict)
    if use_v6:
        ip = Utils.getRealIPv6()
        type = 'AAAA'
    else:
        ip = Utils.getRealIP()
        type = 'A'
    print({'type': type, 'ip':ip})
    if not drDict:
       raise AttributeError("失败！域名字典为空！请检查配置文件")

    for each in drDict.items():
        request = Utils.getCommonRequest()
        request.set_domain('alidns.aliyuncs.com')
        request.set_version('2015-01-09')
        request.set_action_name('UpdateDomainRecord')
        request.add_query_param('RecordId', each[1])
        request.add_query_param('RR', each[0])
        request.add_query_param('Type', type)
        request.add_query_param('Value', ip)
        response = client.do_action_with_exception(request)
        print(each[0]+"域名更新成功！")
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DDNS')
    parser.add_argument('-6', '--ipv6', nargs='*', default=False)
    args = parser.parse_args()
    isipv6 = isinstance(args.ipv6, list)

    try:
        while not Utils.isOnline():
            time.sleep(3)
            continue
        DDNS(isipv6)
        print("成功！")
    except (ServerException,ClientException) as reason:
        print("失败！原因为")
        print(reason.get_error_msg())
        print("可参考:https://help.aliyun.com/document_detail/29774.html?spm=a2c4g.11186623.2.20.fDjexq#%E9%94%99%E8%AF%AF%E7%A0%81")
        print("或阿里云帮助文档")
    except (AttributeError) as reason:
        print(reason)