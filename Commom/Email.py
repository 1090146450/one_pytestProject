# encoding=utf-8
import yagmail


class send_email:
    def emil(self):
        # 建立对象连接
        yag = yagmail.SMTP(user={"an1090146450@163.com": "测试服务器"}, password="HMIJRCNOLTPZCUNW", host="smtp.163.com")
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
