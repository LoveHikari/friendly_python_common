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


# http 请求帮助类
class HttpUtils(object):
    def __init__(self):
        self.__session = requests.session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1'}
        self.__session.headers = headers

    def get(self, url: str) -> str:
        """
        get 请求
        :param url: 请求地址
        :return: 响应文本
        """
        response = self.__session.get(url=url)
        return response.text

    def post(self, url: str, params: dict[str, any]) -> str:
        """
        post 请求
        :param url: 请求地址
        :param params: 请求参数
        :return: 响应文本
        """
        response = self.__session.post(url=url, params=params)
        return response.text

    def set_cookies(self, cookies: str):
        """
        设置 cookies
        :param cookies:
        """
        c = {}
        for coo in filter(None, cookies.split(';')):
            name, value = coo.strip().split('=', 1)
            c[name] = value
        requests.utils.add_dict_to_cookiejar(self.__session.cookies, c)

    def set_headers(self, headers: dict[str, str]):
        """
        设置 headers
        :param headers:
        """
        self.__session.headers = headers

    def set_proxy(self, proxy: str):
        """
        设置代理
        :param proxy: 例: http://127.0.0.1:8889
        """
        proxies = {
            'http': proxy,
            'https': proxy
        }
        self.__session.proxies = proxies
        self.__session.verify = False  # verify是否验证服务器的SSL证书
