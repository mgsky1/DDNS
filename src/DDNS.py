'''
DDNS 主程序 使用阿里云的SDK发起请求
Created By Martin Huang on 2018/5/20
修改记录：
2018/5/20 => 第一版本
2018/5/26 => 增加异常处理、Requst使用单例模式，略有优化
2018/5/29 => 增加网络连通性检测，只有联通时才进行操作，否则等待
2018/6/10 => 使用配置文件存储配置，避免代码内部修改(需要注意Python模块相互引用问题)
2018/9/24 => 修改失败提示信息
2024/7/13 => 修改DDNS函数逻辑，应对同一设备存在多个公网ipv6地址的情况
'''
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkcore.acs_exception.exceptions import ClientException
from Utils import Utils
import time
import argparse

def DDNS(use_v6):
    client = Utils.getAcsClient()
    recordIds = Utils.getRecordId(Utils.getConfigJson().get('Second-level-domain'))
    if use_v6:
        ips = Utils.getRealIPv6()
        type = 'AAAA'
    else:
        ips = [Utils.getRealIP()]   
        type = 'A'
    print({'type': type, 'ip':ips})

    request = Utils.getCommonRequest()
    request.set_domain('alidns.aliyuncs.com')
    request.set_version('2015-01-09')
    request.set_action_name('UpdateDomainRecord')

    used_ips = set()    # 用于跟踪已使用过的IP地址

    for recordId in recordIds:
        for ip in ips:
            if ip in used_ips:
                continue  
            try:
                request.add_query_param('RecordId', recordId)
                request.add_query_param('RR', Utils.getConfigJson().get('Second-level-domain'))
                request.add_query_param('Type', type)
                request.add_query_param('Value', ip)
                used_ips.add(ip)                  
                response = client.do_action_with_exception(request)
                print(f"更新RecordId {recordId} 的IP地址 {ip} 成功！")
                break  
            except (ServerException, ClientException) as reason:
                print(f"更新RecordId {recordId} 的IP地址 {ip} 失败！")
                print("原因为:", reason.get_error_msg())
                print("错误码：", reason.get_error_code())
                print("可参考: https://help.aliyun.com/document_detail/29774.html")
                print("或阿里云帮助文档")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='DDNS')
    parser.add_argument('-6', '--ipv6', nargs='*', default=False)
    args = parser.parse_args()
    isipv6 = isinstance(args.ipv6, list)

    DDNS(isipv6)
    print("完成！")
