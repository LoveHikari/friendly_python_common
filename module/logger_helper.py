#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# @Name    : 模块logger帮助类
# @Purpose : logger帮助
# @Time    : 2019/1/16 12:51
# @Author  : Ifish
# @Site    :
# @File    : logger_helper.py
# @Software: PyCharm
# @Refer   : https://blog.csdn.net/u010986776/article/details/79680969
# -------------------------------------------------------------------------------
import logging
import datetime
import os


class LoggerHelper(object):
    # 获取logger对象,取名mylog
    logger = logging.getLogger("mylog")

    # 输出INFO及以上级别的信息
    logger.setLevel(level=logging.INFO)

    # 获取文件处理器并设置日志级别
    now_time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d')
    file_path = './logs/log_"+now_time+".txt'
    f = os.path.split(file_path)
    if not os.path.exists(f[0]):
        os.makedirs(f[0])
    handler = logging.FileHandler("./logs/log_" + now_time + ".txt")
    handler.setLevel(logging.INFO)

    # 生成并设置文件处理器的日志格式
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(pathname)s %(filename)s[line:%(lineno)d] - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # 获取流处理器并设置日志级别
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # 为logger对象同时添加文件处理器和流处理器
    logger.addHandler(handler)
    logger.addHandler(console)
