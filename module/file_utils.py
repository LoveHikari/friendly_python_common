# -*- coding: UTF-8 -*-
# -------------------------------------------------------------------------------
# Name:        模块file Helper
# Purpose:     http请求帮助
#
# Author:      iccfish
#
# Created:     14-01-2019
# Copyright:   (c) iccfish 2019
# Licence:     <your licence>
# -------------------------------------------------------------------------------


class FileUtils(object):

    @staticmethod
    def read(file_path: str) -> str:
        """
        读文件
        :param file_path: 文件路径
        :return 文件内容
        """
        with open(file_path, "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            return data

    @staticmethod
    def write(file_path: str, txt: str):
        """
        写文件
        :param file_path: 文件路径
        :param txt: 文件内容
        """
        with open(file_path, "w") as f:
            f.write(txt)  # 这句话自带文件关闭功能，不需要再写f.close()
