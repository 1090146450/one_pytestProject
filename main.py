from Commom import Request

data = {"username": "root",
        "passwod": 123}
js = Request.RequestUtil().all_send_request("post", "http://127.0.0.1:8000/api/login",data=data)
print(js.text)
