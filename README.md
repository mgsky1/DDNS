# aliyunDDNS

Get current IP and update the domain resolutions on Aliyun。

## Configuration

Set your configuration in `config.json` and put the file in root path of the project：

```json
{
    "AccessKeyId": "Your_AccessKeyId",
    "AccessKeySecret": "Your_AccessKeySecret",
    "region": "cn-hangzhou", // or your real region
    "First-level-domain": "Your_First-level-domain",
    "Second-level-domain": ['Your', 'Second-level-domains', 'array']
}
```

## Get started

### Linux

run `crontab -e`, then add `*/5 * * * * python3 aliyunDDNS.py now`, save it.
if necessary, run `/etc/init.d/cron restart`.

### Windows

run `python3 aliyunDDNS.py`, it will start a schedule.