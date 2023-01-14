import logging

import pytest

from Params import tools
from Commom import Consts, Request


class Test_Url:
    """测试服务器接口"""
    yaml_login = tools.YamlUtil("Login.yaml")
    yaml_data = yaml_login.read_yaml()
    run_number = 1

    @pytest.mark.parametrize("driver", yaml_data)
    def test_login(self, driver):
        """登录接口测试"""
        # 定义log对象
        logger = logging.getLogger(__name__)
        # 添加LOG
        logger.info(f"开始执行第{Test_Url.run_number}条用例")
        logger.info("读取用例中数据")
        guest_url = Consts.all_url + driver["url"]
        logger.info("URL读取成功,URL:" + str(guest_url))
        data = driver["data"]
        logger.info(f"接口传值:{data}")
        method = driver["method"]
        logger.info(f"请求方式:{method}")
        logger.info(f"开始请求接口")
        try:
            guest_data = Request.RequestUtil().all_send_request(method, guest_url, data=data)
            logger.info(f"接口请求成功")
        except Exception as e:
            logger.error(f"接口请求失败,失败原因如下:{e}\n")
        guest_json = guest_data.json()
        logger.info(f"请求返回数据:{guest_json}")
        for k, v in driver["check"].items():
            logger.info(f"开始校验数据")
            try:
                assert guest_json[k] == v
                logger.info(f"数据校验完成")
            except Exception as e:
                logger.error(f"校验失败:{e}")
        Test_Url.run_number += 1
        logger.info("\n")
