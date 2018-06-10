'''
DDNS 主程序 使用阿里云的SDK发起请求
Created By Martin Huang on 2018/5/20
修改记录：
2018/5/20 => 第一版本
2018/5/26 => 增加异常处理、Requst使用单例模式，略有优化
2018/5/29 => 增加网络连通性检测，只有联通时才进行操作，否则等待
2018/6/10 => 使用配置文件存储配置，避免代码内部修改(需要注意Python模块相互引用问题)
'''
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.acs_exception.exceptions import ClientException
from Utils import Utils
import time

def DDNS():
    client = Utils.getAcsClient()
    recordId = Utils.getRecordId('ddns')
    ip = Utils.getRealIP()
    request = Utils.getCommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')
    request.add_query_param('RecordId', recordId)
    request.add_query_param('RR', Utils.getConfigJson().get('Second-level-domain'))
    request.add_query_param('Type', 'A')
    request.add_query_param('Value', ip)
    response = client.do_action_with_exception(request)
    return response

if __name__ == "__main__":
    try:
        while not Utils.isOnline():
            time.sleep(3)
            continue
        result = DDNS()
        print("成功！")
    except (ServerException,ClientException) as reason:
        print("失败！原因为")
        print(reason.get_error_msg())