# DDNS

[中文](https://github.com/mgsky1/DDNS/blob/master/README_ZH_CN.md) | [English](https://github.com/mgsky1/DDNS/blob/master/README.md)

## Summary

> Implemented using Python and Alibaba Cloud DNS API. Can be used in a home environment to map NAS, DB, Web, and other applications to the public network.

## Install

```bash
pip3 install aliyun-python-sdk-core
```
Tested with aliyun-python-sdk-core==2.15.1 on 2024/07/13.

## Run
```bash
cd src
python3 DDNS.py      # Default to ipv4
python3 DDNS.py -6   # Switch to ipv6
```

## Note
> * Based on: Python 3, Alibaba Cloud Python SDK, Alibaba Cloud DNS API
> * Directly run the main function of the DDNS.py file. The main functions of other .py files are for testing purposes.
> * You can set this script as a system scheduled task, for example, to execute once at 4:30 AM every day or to run automatically each time you connect to the internet.
> * The latest [dev](https://github.com/mgsky1/DDNS/tree/dev) branch adds the feature of binding multiple domain names to the same IP address. Feel free to try it out.
> * If you use an IPv4 address, make sure the record type of the domain is set to **A**. If you use an IPv6 address, set it to **AAAA**.
> * This script is a personal implementation of DDNS.

## Restrict
> This script is suitable for home broadband with dynamic IP. If not, you can use NAT-DDNS tools like [frp](https://github.com/fatedier/frp) for intranet penetration.

## Configuration
This project has been modified to store user configurations using a configuration file. The configuration file is in JSON format and is stored in config.json, as shown below:
```
{
    "AccessKeyId": "Your_AccessKeyId", // Your Alibaba Cloud AccessKeyId
    "AccessKeySecret": "Your_AccessKeySecret", // Your Alibaba Cloud AccessKeySecret
    "First-level-domain": "Your_First-level-domain", // First-level domain, e.g., example.com
    "Second-level-domain": "Your_Second-level-domain" // Second-level domain, e.g., ddns.example.com, just enter ddns, or use @ to directly resolve the primary domain
}
```

## Tip
> How to determine if your broadband has a dynamic IP:
> * Step 1: Search for your IP on Baidu to find your IP address.
> * Step 2: Start a local website, for example, start IIS on Windows or install Apache or Nginx on Linux and start it with their default page.
> * Step 3: Set up port forwarding rules on the router. It is best not to use port 80 for public IP network access as it may be blocked by the ISP.
> * Step 4: Finally, use the public IP + port number found earlier to access and see if you can display the intranet page. If so, congratulations!

## ScreenShots

Note: Since I have already updated, it prompts that the IP address already exists. Alibaba Cloud does not allow the same IP to be updated repeatedly. The second image is local, and the third image is external network.<br/>
![](http://xxx.fishc.org/forum/201805/26/181341tp2frcnnnvnvc5iz.png)

![](http://xxx.fishc.org/forum/201805/26/200124rsubrwwdblr8ffwz.png)

![](http://xxx.fishc.org/forum/201805/26/200228kb1u63hargn0pc1n.png)

## Change Log
> * 2018/5/29 Network connectivity check, only operate when there is a network, otherwise wait for network connection.
> * 2018/6/10 Use configuration file to store user data.
> * 2018/9/24 Modify failure prompt output, add Alibaba help URL for users to check corresponding error information.
> * 2018/12/24 Improve IP acquisition method, remove BS4 dependency, thanks to [@Nielamu](https://github.com/NieLamu).
> * 2018/12/27 Add IPv6 support, thanks to [@chnlkw](https://github.com/chnlkw).
> * 2020/05/05 Modify IPv4 address acquisition method. If it fails, it will be logged and retried in 10 seconds using a new method. Thanks to [@sunsheho](https://github.com/sunsheho).
> * 2024/07/13 Add a method to get IPv6 address using ifconfig to handle the situation where the same device has multiple public IPv6 addresses.

## Contribution
Feel free to fork the project if interested, and if you have any questions, feel free to ask in the issue section~