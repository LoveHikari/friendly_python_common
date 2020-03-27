# -*- coding: utf-8 -*-

import inspect
import ctypes
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *


# 继承QThread
class runthread(QtCore.QThread):
    # python3,pyqt5与之前的版本有些不一样
    #  通过类成员对象定义信号对象
    _signal = pyqtSignal() #type:PyQt5.QtCore.pyqtSignal.pyqtSignal

    def __init__(self, parent=None):
        super(runthread, self).__init__()

    def __del__(self):
        self.wait()

    def run(self):
        # 处理你要做的业务逻辑，这里是通过一个回调来处理数据，这里的逻辑处理写自己的方法
        # wechat.start_auto(self.callback)
        self._signal.emit()  #可以在这里写信号焕发

    # def callback(self, msg):
    #     # 信号焕发，我是通过我封装类的回调来发起的
    #     self._signal.emit(msg)

    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    # 关闭线程
    def stop_thread(self, thread):
        self._async_raise(thread.ident, SystemExit)
