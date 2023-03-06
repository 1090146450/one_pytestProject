from Commom import Request

data = {"username": "root",
        "password": 123}
js = Request.RequestUtil().all_send_request("post", "http://abc.twoitmen.club/api/login",data=data)
print(js.text)
