import logging

import allure

from Params import tools
from Commom import Consts, Request
from Commom.Logger import ApiAutoLogin
import pytest


class Test_Url:
    """测试服务器接口"""
    yaml_login = tools.YamlUtil("Login.yaml")  # 读取yaml文件
    yaml_data = yaml_login.read_yaml()  # 获取yaml文件中的数据
    # 定义log对象
    logger = ApiAutoLogin()

    @pytest.mark.parametrize("driver", yaml_data)
    @allure.title()
    def test_login(self, driver):
        """登录接口测试"""
        # 添加LOG
        title = driver["title"]
        Test_Url.logger.info(f"开始执行用例,标题:{title}")
        Test_Url.logger.info("读取用例中数据")
        guest_url = Consts.all_url + driver["url"]  # 获取URL
        Test_Url.logger.info("URL读取成功,URL:" + str(guest_url))
        data = driver["data"]  # 获取数据驱动中的数据
        Test_Url.logger.info(f"接口传值:{data}")
        method = driver["method"]  # 获取请求方式
        Test_Url.logger.info(f"请求方式:{method}")
        Test_Url.logger.info(f"开始请求接口")
        try:
            guest_data = Request.RequestUtil().all_send_request(method, guest_url, data=data)  # 开始请求接口
            Test_Url.logger.info(f"接口请求成功")
        except Exception as e:
            Test_Url.logger.debug(f"接口请求失败,失败原因如下:{e}\n")
        guest_json = guest_data.json()  # 获取返回的JSON
        Test_Url.logger.info(f"请求返回数据:{guest_json}")
        for k, v in driver["check"].items():
            Test_Url.logger.info(f"开始校验数据")
            try:
                assert guest_json[k] == v  # 对返回数据和数据驱动中数据进行校验
                Test_Url.logger.info(f"数据校验完成")
            except Exception as e:
                Test_Url.logger.debug(f"校验失败:{e}")
                raise e
        Test_Url.logger.info("\n")
