import logging
import time

import allure
import win32_setctime

from Params import tools
from Commom import Consts, Request
from Commom.Logger import ApiAutoLogin, MemoryLog
import pytest


@allure.epic("接口测试用例")
@allure.feature("登录模块")
class Test_Url:
    """测试服务器接口"""
    yaml_login = tools.YamlUtil("Login.yaml")  # 读取yaml文件
    yaml_data = yaml_login.read_yaml()  # 获取yaml文件中的数据
    # 定义log对象
    logger = ApiAutoLogin()

    # logger = logging.getLogger(__name__)

    @pytest.fixture()
    def drse(self):
        """等待4S"""
        yield time.sleep(4)

    @pytest.fixture(scope="function")
    def dr(self):
        """保存打印LOG"""
        m = MemoryLog()
        yield m
        m.preservation()

    @pytest.mark.parametrize("driver", yaml_data)
    @allure.title("登录接口测试")
    @allure.step("步骤")
    def test_login(self, driver, dr, drse):
        """登录接口测试"""
        # 添加LOG
        title = driver["title"]
        dr.add(f"开始执行用例,标题:{title}")
        dr.add("读取用例中数据")
        with allure.step("获取URL"):
            guest_url = Consts.all_url + driver["url"]  # 获取URL
        dr.add("URL读取成功,URL:" + str(guest_url))
        with allure.step("获取测试数据"):
            data = driver["data"]  # 获取数据驱动中的数据
        dr.add(f"接口传值:{data}")
        with allure.step("获取请求方式"):
            method = driver["method"]  # 获取请求方式
        dr.add(f"请求方式:{method}")
        dr.add(f"开始请求接口")
        try:
            with allure.step("开始请求接口"):
                guest_data = Request.RequestUtil().all_send_request(method, guest_url, data=data)  # 开始请求接口
            dr.add(f"接口请求成功")
        except Exception as e:
            dr.add(f"接口请求失败,失败原因如下:{e}\n")
        guest_json = guest_data.json()  # 获取返回的JSON
        dr.add(f"请求返回数据:{guest_json}")
        for k, v in guest_json.items():
            dr.add(f"开始校验数据")
            try:
                with allure.step("开始校验数据"):
                    assert driver["check"][k] == v  # 对返回数据和数据驱动中数据进行校验
                dr.add(f"数据校验完成")
            except Exception as e:
                dr.add(f"校验失败:{e}")
                raise e


    @allure.step("步骤2")
    def test_1(self):
        assert 1 == 1
