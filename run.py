# coding=utf-8
from Commom import Email
import os
import pytest

pytest.main()
os.system("allure serve Report")
Email.send_email().emil()
print("邮件发送成功")
