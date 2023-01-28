# coding=UTF-8
import os
from datetime import datetime
from io import StringIO

from loguru import logger


class ApiAutoLogin:
    """logo文件封装"""

    def __new__(cls, *args, **kwargs):
        """修改默认参数"""
        longname = datetime.now().strftime("%Y-%m-%d")  # 获取当前时间
        sink = os.getcwd() + f"/logs/{longname}.log"  # 日志名称
        level = "DEBUG"  # 日志等级
        encoding = "gbk"  # 编码
        enqueue = True  # 是否多线程保护
        rotation = "20MB"  # 支持多大
        retention = "1 week"  # 保留1星期
        logger.add(sink=sink, level=level, encoding=encoding, enqueue=enqueue, rotation=rotation, retention=retention)
        return logger


class MemoryLog:
    """在内存中写入log"""
    open_state = 0

    def __init__(self, moder="a"):
        self.f = StringIO()
        self.moder = moder

    def info(self, data):
        """写入info数据"""
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
        if not isinstance(data, str):
            data = str(data)
        data = "info " + data
        self.f.write(log_time + data + "\n")

    def error(self, data):
        """写入error数据"""
        log_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S ")
        if not isinstance(data, str):
            data = str(data)
        data = "error " + data
        self.f.write(log_time + data + "\n")

    def preservation(self):
        """保存数据"""
        longname = datetime.now().strftime("%Y-%m-%d")  # 获取当前时间
        sink = os.getcwd() + f"/logs/{longname}.log"
        if (self.moder == "w" or self.moder == "w+") and MemoryLog.open_state == 0:
            with open(sink, mode="w+", encoding="GBK"):
                MemoryLog.open_state == 1

        with open(sink, mode="a", encoding="GBK") as t:
            t.write(self.f.getvalue())
        self.f.close()
