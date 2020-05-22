'''
获取用户真实IP地址
Created By Martin Huang on 2018/5/19
修改记录：
2018/12/24 =》改进ip获取方式 取消BS4依赖 感谢@Nielamu的建议
2020/05/05 =》改进ipv4获取方式，如果获取失败，则会写入日志文件，并过10秒后使用新的网址重试，感谢@sunsheho贡献的代码
			  我在休眠时间上略作修改
'''
import urllib.request
from urllib import request,error
import json
import time,datetime
from time import sleep

def senderror(errcont):
	enow=datetime.datetime.now()
	now=enow.strftime('%Y-%m-%d %H:%M:%S')
	errfile=open('DDNS.log','a')
	errfile.write(now)
	errfile.write(str(errcont))
	errfile.write('\n')
	errfile.close()



def getIpPage():
	try:
		url = "https://api.ipify.org/?format=json"
		response = request.urlopen(url,timeout=60)
		html = response.read().decode('utf-8')
		return html
	except error.HTTPError as e:
		print(e.reason)
		senderror(e.reason)
		time.sleep(10)
		getIpPage()
	except error.URLError as e:
		print(e.reason)
		senderror(e.reason)
		time.sleep(10)
		getIpPage()
	except:
		url = "http://members.3322.org/dyndns/getip"
		response = request.urlopen(url,timeout=60)
		html = response.read().decode('utf-8')
		html = html.replace("\n","")
		htm={}
		htm['ip'] = html
		HTL = json.dumps(htm)
		return HTL

# 解析数据，获得IP
def getRealIp(data):
	try:
		jsonData = json.loads(data)
		return jsonData['ip']
	except:
		time.sleep(200)
		getIpPage()


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
