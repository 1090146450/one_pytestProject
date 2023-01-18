# coding=UTF-8
import os
from datetime import datetime

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