import requests
from Commom import Consts


class RequestUtil:
    """设置类变量sess保证携带session接口请求"""
    sess = requests.session()

    def __init__(self):
        # 添加请求头
        self.header = {"User-Agent": Consts.Agent}

    def all_send_request(self, method, *args, headers=None, **kwargs):
        """填写请求的方法和其他参数"""
        if headers is not None:
            print(headers, self.header)
            try:
                self.header = dict(**self.header, **headers)
            except Exception as e:
                raise e
        methon_list = ["get", "post", "put", "delete"]
        if method not in methon_list:
            raise Exception("请填写正确的请求方式")
        res = RequestUtil.sess.request(method, *args, headers=self.header, **kwargs)
        return res
