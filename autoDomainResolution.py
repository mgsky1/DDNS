#!/usr/bin/env python3
# encoding: utf-8


import time
import sys
import os
import schedule


from Utils import Utils


ipHistoryJson = 'ipHistory.json'
configJSON = 'config.json'


def checkAndUpdateDomain():
    newIp = Utils.getRealIp()
    print('newIp', newIp)

    if not os.path.exists(ipHistoryJson):
        Utils.setJson(ipHistoryJson, {"ip":""})

    oldData = Utils.getJson(ipHistoryJson)
    if oldData['ip'] != newIp:
        print('need uppdate from %s to %s '%(oldData['ip'], newIp))
        result = Utils.DDNS(configJSON, newIp)
        if result:
            oldData['ip'] = newIp
            Utils.setJson(ipHistoryJson, oldData)


print('starting1...')


if __name__ == "__main__":

    print('starting2...')

    if len(sys.argv) > 1 and sys.argv[1] == 'now':
        print('not scheduled.')
        checkAndUpdateDomain()
    else:
        print('task scheduled.')

        schedule.every(1).minutes.do(checkAndUpdateDomain)

        while True:
            schedule.run_pending()
            time.sleep(1)

    pass
