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


class MemoryLog():
    """在内存中写入log"""

    def __init__(self):
        self.f = StringIO()

    def add(self, data):
        """写入数据"""
        if not isinstance(data, str):
            raise Exception("请输入字符串")
        self.f.write(data + "\n")

    def preservation(self):
        """保存数据"""
        longname = datetime.now().strftime("%Y-%m-%d")  # 获取当前时间
        sink = os.getcwd() + f"/logs/{longname}.log"
        with open(sink, mode="a", encoding="GBK") as t:
            t.write(self.f.getvalue())

