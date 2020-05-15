# DDNS
[中文](https://github.com/mgsky1/DDNS/blob/master/README_ZH_CN.md)|[English](https://github.com/mgsky1/DDNS/blob/master/README.md)
## Summary
> Python and Aliyun SDK API have been used in this project. You can use this tool to map the local applications like NAS, DB, WEB etc to the internet.
## Install
```bash
pip3 install aliyun-python-sdk-core-v3
```
## Run
```bash
python3 src/DDNS.py      # default ipv4
python3 src/DDNS.py -6   # change to ipv6
```
## Note
> * Based on Python3、Aliyun API.
> * To begin, you can run the main function in DDNS.py. The main function in other .py files are for the test purpose.
> * You can set this script as a timer task in your opening system. For example, running this script at 4:30am everyday or when connecting to the internet.
> * On the [dev](https://github.com/mgsky1/DDNS/tree/dev) branch, this project supports binding multiple domains to the same ip address.
> * If you use iPv4, please make sure that the record type of your domain which will be used is **A**. If you use iPv6, the type is **AAAA**. 
> * This script is my idea for implementing DDNS.

## Restrict
> This script is suitable for the broadband which has a dynamic IP. If not, you can try NAT-DDNS tools like [frp](https://github.com/fatedier/frp).

## Configuration
The config.json has some infomation you should provide. The config structure may like this: 
```
{
    "AccessKeyId": "Your_AccessKeyId",//Your Aliyun AccessKeyId
    "AccessKeySecret": "Your_AccessKeySecret",//Your Aliyun AccessKeySecret
    "First-level-domain": "Your_First-level-domain",//First level domain, eg example.com
    "Second-level-domain": "Your_Second-level-domain"//Second level domain, eg ddns.example.com Just input ddns
}
```
## Tip
> How to determine wether your broadband service has a dynamic IP.
> * Step 1：Find your WAN IP by google or other tools.
> * Step 2：Run a web service locally. For example, starting IIS in Windows or Apache in Linux and using their default webpage.
> * Step 3: Set the map rules in your home router. The ports which you will use to access the local service over internet had better not to be 80 beacuse the 80 port may be blocked by your internet service provider.
> * Step 4: Use the IP you fond by google and the port to access your local web service. If ok, congratulations！

## ScreenShots
NOTE: Because I have updated before, the script tells me the DNS record has already exists. Aliyun does not allow users to update the same IP when the IP has not been changed. The second picture shows the local service. The Third one shows accessing local service over internet under the help of DDNS.

![](http://xxx.fishc.org/forum/201805/26/181341tp2frcnnnvnvc5iz.png)

![](http://xxx.fishc.org/forum/201805/26/200124rsubrwwdblr8ffwz.png)

![](http://xxx.fishc.org/forum/201805/26/200228kb1u63hargn0pc1n.png)

## Change Log
> * 2018/5/29 Add detecting internet access.
> * 2018/6/10 Start using configuration file.
> * 2018/9/24 Improve the error output
> * 2018/12/24 Improve the way to get IP, deleteing BS4 dependence. Thanks @Nielamu.
> * 2018/12/27 Support ipv6. Thanks @chnlkw.

## Contribution
If you interest in this project and want to improve it, welcome to fork the project. Have any questions? you can ask in issue~
