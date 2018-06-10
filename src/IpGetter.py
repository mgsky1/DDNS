'''
获取用户真实IP地址
Created By Martin Huang on 2018/5/19
'''
import urllib.request
import re
from bs4 import BeautifulSoup

#从ip138爬取探测用户实际ip的网页
def getIpPage():
    url = "http://www.ip138.com/"
    response = urllib.request.urlopen(url)
    html = response.read().decode("gb2312")
    soup = BeautifulSoup(html, "lxml")
    _iframe = soup.body.iframe
    return _iframe["src"]

#解析网页，正则判断，获取用户实际公网ip
def getRealIp(url):
    response = urllib.request.urlopen(url)
    html = response.read().decode("gb2312")
    pattern = r"(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)\.(25[0-5]|2[0-4]\d|[0-1]\d{2}|[1-9]?\d)"
    matchs = re.search(pattern,html)
    ip_addr = ""
    for i in range(1,5):
        ip_addr += matchs.group(i) + "."
    return ip_addr[:-1]