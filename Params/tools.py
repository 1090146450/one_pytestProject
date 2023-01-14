"""yaml文件处理"""
import glob
import os

import yaml


class YamlUtil:

    def __init__(self, file_name):
        """传入要打开文件"""
        file_route = os.getcwd() + "\\Params\\" + file_name
        if glob.glob(file_route):
            self.file_route = file_route
        else:
            raise Exception(f"您输入的路径为:{file_route}"+"请检查文件路径")

    def read_yaml(self):
        """读取yaml文件"""
        with open(self.file_route, encoding="utf-8",mode="r") as f:
            val = yaml.load_all(stream=f, Loader=yaml.FullLoader)
            return [i for i in val]

    def write_yaml(self, data):
        """写入yaml文件"""
        with open(self.file_route, encoding="utf-8", mode="a") as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def clean_yaml(self):
        """清空文件"""
        with open(self.file_route,encoding="utf-8",mode="w") as f:
            f.truncate()