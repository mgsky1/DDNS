# DDNS

[中文](https://github.com/mgsky1/DDNS/blob/master/README_ZH_CN.md)|[English](https://github.com/mgsky1/DDNS/blob/master/README.md)

## Summary

> 利用Python和阿里云云解析API实现。可利用于家庭环境，向公网映射NAS，DB，Web等应用

## Install

```bash
pip3 install aliyun-python-sdk-core
```
aliyun-python-sdk-core==2.15.1  2024/07/13测试通过

## Run
```bash
cd src
python3 DDNS.py      # 默认ipv4
python3 DDNS.py -6   # 改用ipv6
```


## Note
> * 基于：Python 3 、阿里云Python SDK、阿里云云解析API
> * 直接运行DDNS.py文件的main函数即可，其他的py文件的main函数都为测试
> * 可将此脚本设置为系统定时任务，例如每天凌晨4:30执行一次或者每次联网时自动执行一次
> * *在最新的[dev](https://github.com/mgsky1/DDNS/tree/dev)分支中增加了同一IP同时绑定多个域名的功能，欢迎体验*
> * 如果您使用iPv4地址，请确保域名的记录类型设置为**A**，如果是要使用iPv6，设置成**AAAA**
> * 此脚本为DDNS实现的个人想法

## Restrict
> 本脚本适用于家庭宽带IP为动态IP的情形，若不是，可以利用[frp](https://github.com/fatedier/frp)等NAT-DDNS内网穿透工具
## Configuration
本项目修改为使用配置文件方式存储用户配置，配置文件为JSON格式，存放于config.json文件中，形式如下：
```
{
    "AccessKeyId": "Your_AccessKeyId",//你的阿里云AccessKeyId
    "AccessKeySecret": "Your_AccessKeySecret",//你的阿里云AccessKeySecret
    "First-level-domain": "Your_First-level-domain",//一级域名，例如 example.com
    "Second-level-domain": "Your_Second-level-domain"//二级域名，例如 ddns.example.com 填入ddns即可，也可使用@表示直接解析主域名
}
```
## Tip
> 判断自家宽带是否是动态IP的方式：
> * Step 1：百度搜索IP，查到自己的IP地址
> * Step 2：接着本地开一个网站，比如在Windows下直接启动IIS，Linux下安装一个Apache或者Nginx启动，使用它们的默认页面
> * Step 3：然后在路由器上设置好转发规则，公网IP的网络访问端口最好不要用80，80端口可能被运营商封了
> * Step 4：最后利用前面查到的公网IP+端口号访问一下，看看能不能显示内网上的页面，如果可以，恭喜你！
## ScreenShots

注：因为我已经更新过了，所以它提示IP地址已存在，阿里云是不允许同一个IP重复更新的。第二张图为本地，第三张图为外网<br/>
![](http://xxx.fishc.org/forum/201805/26/181341tp2frcnnnvnvc5iz.png)

![](http://xxx.fishc.org/forum/201805/26/200124rsubrwwdblr8ffwz.png)

![](http://xxx.fishc.org/forum/201805/26/200228kb1u63hargn0pc1n.png)

## Change Log
> * 2018/5/29 网络连通性检测，只有在有网时才进行操作，否则等待网络连接
> * 2018/6/10 启用配置文件存储用户数据
> * 2018/9/24 修改失败提示输出，添加阿里帮助网址，让用户可查询错误对应信息
> * 2018/12/24 改进ip获取方式，删除BS4依赖，感谢[@Nielamu](https://github.com/NieLamu)
> * 2018/12/27 增加ipv6支持，感谢[@chnlkw](https://github.com/chnlkw)
> * 2020/05/05 修改ipv4地址获取方式。如果失败，会写入日志，并在10秒后采用新的方式重试。感谢[@sunsheho](https://github.com/sunsheho)
> * 2024/07/13 添加使用ifconfig获取ipv6地址的方式，能够应对同一设备拥有多个公网ipv6地址的情况

## Contribution
如果感兴趣欢迎fork项目，如果有任何问题欢迎在issue区提问~

