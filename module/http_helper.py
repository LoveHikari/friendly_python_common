# -*- coding: UTF-8 -*-
# -------------------------------------------------------------------------------
# Name:        模块http Helper
# Purpose:     http请求帮助
#
# Author:      iccfish
#
# Created:     14-01-2019
# Copyright:   (c) iccfish 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import requests
from module.logger_helper import LoggerHelper

# http 请求帮助类
class HttpHelper(object):

    # def post(self,money, bank_mark):
    #     reqheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1' }
    #     # 定义post的参数
    #     reqdata = {'money': (None,money),
    #                'key': (None,'12345678'),
    #                'bank_mark': (None,bank_mark)
    #                }
    #     url='http://47.99.199.184/server/alipayAutomatic/uploadOrder'
    #     r = requests.post(url,files=reqdata,headers=reqheaders)
    #     print(r.text)
    @staticmethod
    def post(url: str, data: dict[str, str]) -> str:
        """
        post 请求
        :param url: 请求地址
        :param data: 请求参数
        :return: 响应文本
        """
        r = None
        try:
            reqheaders = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
            r = requests.post(url, files=data, headers=reqheaders)
        except Exception as e:
            print(e)
            LoggerHelper.logger.info(e)
        finally:
            if r is None:
                return ''
            else:
                if r.status_code == 200:
                    print(r.text)
                    return r.text
                else:
                    LoggerHelper.logger.info(str(r.status_code) + ': ' + r.reason)
                    # raise Exception(str(r.status_code) + ': ' + r.reason)
                    return ''



