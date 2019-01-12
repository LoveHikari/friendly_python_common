# coding=utf-8

import requests
#http 请求帮助类
class httpHelper(object):
    @staticmethod
    def post(url:str,reqdata:dict[str, str]):
        '''
        post 请求
        :param url: 请求地址
        :param reqdata: 请求参数
        :return: 响应文本
        '''
        reqheaders = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1' }
        r = requests.post(url,files=reqdata,headers=reqheaders)
        return r.text
