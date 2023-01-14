import os
from Params import tools
from Commom import Consts, Request
import requests
yamlUt = tools.YamlUtil("Login.yaml")
yaml_data = yamlUt.read_yaml()[4]
guest_url = Consts.all_url + yaml_data["url"]
data = yaml_data["data"]
method = yaml_data["method"]
guest_data = Request.RequestUtil().all_send_request(method, guest_url, data=data)
status = yaml_data["check"]
guest_json = guest_data.json()

print(guest_json,yaml_data["check"])

