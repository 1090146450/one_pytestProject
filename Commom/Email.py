# encoding='utf-8'
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class send_email:
    def emil(self):
        msg = MIMEMultipart()
        msg['Subject'] = "222"
        msg['From'] = "an1090146450@163.com"
        msg['To'] = "1090146450@qq.com"
        content = "<html><h1></h1></html>"
        msg.attach(MIMEText(content, 'html', 'utf-8'))
        # 创建SMTP对象
        smtpObj = smtplib.SMTP()
        # 获取连接指定服务器 填写的就是邮箱SMTP的连接地址和端口号
        smtpObj.connect("smtp.163.com", "25")
        # 登录邮箱和授权码
        smtpObj.login("an1090146450@163.com", "HMIJRCNOLTPZCUNW")
        # 发件人地址，收件人地址可以为列表字符串["1XX@qq.com","2XX@qq.com"]，
        # 邮件内容:一般是msg.as_string():是将msg(MIMEText对象或者MIMEMultipart对象)变为str。
        smtpObj.sendmail("an1090146450@163.com", "1090146450@qq.com", msg.as_string())
        # 退出
        smtpObj.quit()
