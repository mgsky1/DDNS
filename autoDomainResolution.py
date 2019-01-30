#!/usr/bin/env python3
# encoding: utf-8


import time
import sys
import os
import schedule
import logging


from Utils import Utils


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
# StreamHandler
stream_handler = logging.StreamHandler(sys.stdout)
stream_handler.setLevel(level=logging.DEBUG)
logger.addHandler(stream_handler)


ipHistoryJson = 'ipHistory.json'
configJSON = 'config.json'


def checkAndUpdateDomain():
    newIp = Utils.getRealIp()
    logger.info('newIp %s', newIp)

    if not os.path.exists(ipHistoryJson):
        Utils.setJson(ipHistoryJson, {"ip":newIp})

    oldData = Utils.getJson(ipHistoryJson)
    if oldData['ip'] != newIp:
        logger.info('need uppdate from %s to %s '%(oldData['ip'], newIp))
        result = Utils.DDNS(configJSON, newIp)
        if result:
            oldData['ip'] = newIp
            Utils.setJson(ipHistoryJson, oldData)


logger.info('starting1...')


if __name__ == "__main__":

    logger.info('starting2...')

    if len(sys.argv) > 1 and sys.argv[1] == 'now':
        logger.warn('not scheduled.')
        checkAndUpdateDomain()
    else:
        logger.info('task scheduled.')

        schedule.every(5).minutes.do(checkAndUpdateDomain)

        while True:
            schedule.run_pending()
            time.sleep(1)

    pass
