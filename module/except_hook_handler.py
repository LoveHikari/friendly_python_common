# -*- coding: UTF-8 -*-
# -------------------------------------------------------------------------------
# Name:        模块except hook handler
# Purpose:     全局捕获异常
#
# Author:      ankier
#
# Created:     17-08-2013
# Copyright:   (c) ankier 2013
# Licence:     <your licence>
# -------------------------------------------------------------------------------

import logging
import sys
import traceback
import datetime


# 创建记录异常的信息
class ExceptHookHandler(object):
    def __init__(self, log_file, main_frame=None):
        """
        构造函数
        :param log_file: log的输入地址
        :param main_frame: 是否需要在主窗口中弹出提醒
        """
        self.__log_file = log_file
        self.__main_frame = main_frame

        self.__logger = self.__build_logger()
        # 重定向异常捕获
        sys.excepthook = self.__handle_exception

    def __build_logger(self):
        """
        创建logger
        :return:
        """
        logger = logging.getLogger()
        logger.setLevel(logging.DEBUG)
        logger.addHandler(logging.FileHandler(self.__log_file))
        return logger

    def __handle_exception(self, exc_type, exc_value, tb):
        """
        捕获及输出异常
        :param exc_type: 异常类型
        :param exc_value: 异常对象
        :param tb: 异常的trace back
        :return:
        """
        # first logger
        try:
            current_time = datetime.datetime.now()
            self.__logger.info('Timestamp: %s' % (current_time.strftime("%Y-%m-%d %H:%M:%S")))
            self.__logger.error("Uncaught exception：", exc_info=(exc_type, exc_value, tb))
            self.__logger.info('\n')
        except Exception as ex:
            pass

        # then call the default handler
        sys.__excepthook__(exc_type, exc_value, tb)

        err_msg = ''.join(traceback.format_exception(exc_type, exc_value, tb))
        err_msg += '\n Your App happen an exception, please contact administration.'
        # Here collecting traceback and some log files to be sent for debugging.
        # But also possible to handle the error and continue working.
        # dlg = wx.MessageDialog(None, err_msg, 'Administration', wx.OK | wx.ICON_ERROR)
        # dlg.ShowModal()
        # dlg.Destroy()
