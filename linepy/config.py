# -*- coding: utf-8 -*-
from akad.ttypes import ApplicationType
import re

class Config(object):
    LINE_HOST_DOMAIN            = 'https://gd2.line.naver.jp'
    LINE_OBS_DOMAIN             = 'https://obs-sg.line-apps.com'
    LINE_TIMELINE_API           = 'https://gd2.line.naver.jp/mh/api'
    LINE_TIMELINE_MH            = 'https://gd2.line.naver.jp/mh'

    LINE_LOGIN_QUERY_PATH       = '/api/v4p/rs'
    LINE_AUTH_QUERY_PATH        = '/api/v4/TalkService.do'

    LINE_API_QUERY_PATH_FIR     = '/S4'
    LINE_POLL_QUERY_PATH_FIR    = '/P4'
    LINE_CALL_QUERY_PATH        = '/V4'
    LINE_CERTIFICATE_PATH       = '/Q'
    LINE_CHAN_QUERY_PATH        = '/CH4'
    LINE_SQUARE_QUERY_PATH      = '/SQS1'
    LINE_SHOP_QUERY_PATH        = '/SHOP4'
    LINE_LIFF_QUERY_PATH        = '/LIFF1'    
    CHANNEL_ID = {
        'LINE_TIMELINE': '1341209850',
        'LINE_WEBTOON': '1401600689',
        'LINE_TODAY': '1518712866',
        'LINE_STORE': '1376922440',
        'LINE_MUSIC': '1381425814',
        'LINE_SERVICES': '1459630796'
    }

    APP_VERSION = {
    'ANDROID': '11.11.0',
    'IOS': '11.15.0',
    'ANDROIDLITE': '2.17.1',
    'BIZANDROID': '2.13.0',
    'BIZIOS': '2.16.1',
    'BIZWEB': '2.6.1',
    'DESKTOPWIN': '7.0.3',
    'DESKTOPMAC': '7.0.3',
    'IOSIPAD': '11.15.0',
    'CHROMEOS': '2.4.1',
    'WIN10': '6.0.3',
    'DEFAULT': '11.11.0'
}

    APP_TYPE    = 'IOS'
    APP_VER     = APP_VERSION.get(APP_TYPE, APP_VERSION['DEFAULT'])
    CARRIER     = '51089, 1-0'
    SYSTEM_NAME = 'iOS'
    SYSTEM_VER  = '15.4.2'
    IP_ADDR     = '8.8.8.8'
    EMAIL_REGEX = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")

    def __init__(self, appType=None):
        if appType:
            self.APP_TYPE = appType
            self.APP_VER = self.APP_VERSION[self.APP_TYPE] if self.APP_TYPE in self.APP_VERSION else self.APP_VERSION['DEFAULT']
        self.APP_NAME = '%s\t%s\t%s\t%s' % (self.APP_TYPE, self.APP_VER, self.SYSTEM_NAME, self.SYSTEM_VER)
        self.USER_AGENT = 'Line/%s' % self.APP_VER
