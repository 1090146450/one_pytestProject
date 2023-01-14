import requests


class RequestUtil:
    """设置类变量sess保证携带session接口请求"""
    sess = requests.session()

    def all_send_request(self, method, *args,**kwargs):
        """填写请求的方法和其他参数"""
        methon_list = ["get", "post","put","delete"]
        if method not in methon_list:
            raise Exception("请填写正确的请求方式")
        res = RequestUtil.sess.request(method, *args,**kwargs)
        return res
