'''
获取用户真实IP地址
Created By Martin Huang on 2018/5/19
修改记录：
2018/12/24 =》改进ip获取方式 取消BS4依赖 感谢@Nielamu的建议
2018/12/27 =》增加参数-6，用于更新ipv6的记录 感谢@Li Kaiwei
'''
import urllib.request
import json


# 利用API获取含有用户ip的JSON数据
def getIpPage():
    url = "https://api.ipify.org/?format=json"
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html


# 解析数据，获得IP
def getRealIp(data):
    jsonData = json.loads(data)
    return jsonData['ip']


# 利用API获取含有用户ip的JSON数据
def getIpPageV6():
    url = "https://v6.ident.me/.json"
    response = urllib.request.urlopen(url)
    html = response.read().decode('utf-8')
    return html


# 解析数据，获得IP
def getRealIpV6(data):
    jsonData = json.loads(data)
    return jsonData['address']
