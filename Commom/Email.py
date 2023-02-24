# encoding=utf-8
import yagmail
from Params import tools


class send_email:
    def emil(self):
        email_yam = tools.YamlUtil("", file="./Config/passwd.yaml").read_yaml()
        # 建立对象连接
        yag = yagmail.SMTP(user={email_yam[0]["email_account"]: "测试服务器"}, password=email_yam[0]["email_passwd"],
                           host="smtp.qq.com")
        # 收件人
        to = ["1090146450@qq.com"]
        # 邮件主题
        title = "测试邮件"
        # 邮件正文
        cont = "这是一个测试的邮件，请勿回复"
        # 附件列表
        atta = "这里填写路径"
        # 抄送联系人
        cc = "2933310375@qq.com"
        # 邮件发送
        yag.send(to=to, subject=title, contents=cont, cc=cc)
        # 关闭邮件
        yag.close()
