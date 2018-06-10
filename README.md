# DDNS

## Summary

> 利用Python和阿里云云解析API实现。可利用于家庭环境，向公网映射NAS，DB，Web等应用
## Note
> * 基于：Python 3 、阿里云Python SDK、阿里云云解析API、BeautifulSoup 4
> * 你的阿里云的AccessKeyId和AccessKeySecret填充在`AcsClientSingleton.py`文件中
> * 你的域名填充在`Utils.py`中，替换example.com
> * 直接运行DDNS.py文件的main函数即可，其他的py文件的main函数都为测试
> * 可将此脚本设置为系统定时任务，例如每天凌晨4:30执行一次或者每次联网时自动执行一次
> * 此脚本为DDNS实现的个人想法
## Restrict
> 本脚本适用于家庭宽带IP为动态IP的情形，若不是，可以利用[frp](https://github.com/fatedier/frp)等NAT-DDNS内网穿透工具
## Configuration
本项目修改为使用配置文件方式存储用户配置，配置文件为JSON格式，形式如下：
```
{
    "AccessKeyId": "Your_AccessKeyId",//你的阿里云AccessKeyId
    "AccessKeySecret": "Your_AccessKeySecret",//你的阿里云AccessKeySecret
    "First-level-domain": "Your_First-level-domain",//一级域名，例如 example.com
    "Second-level-domain": "Your_Second-level-domain"//二级域名，例如 ddns.example.com 填入ddns即可
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
![](http://xxx.fishc.com/forum/201805/26/181341tp2frcnnnvnvc5iz.png)

![](http://xxx.fishc.com/forum/201805/26/200124rsubrwwdblr8ffwz.png)

![](http://xxx.fishc.com/forum/201805/26/200228kb1u63hargn0pc1n.png)

## Version Log
> * 2018/5/29 网络连通性检测，只有在有网时才进行操作，否则等待网络连接