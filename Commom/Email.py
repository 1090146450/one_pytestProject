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
        # ����SMTP����
        smtpObj = smtplib.SMTP()
        # ��ȡ����ָ�������� ��д�ľ�������SMTP�����ӵ�ַ�Ͷ˿ں�
        smtpObj.connect("smtp.163.com", "25")
        # ��¼�������Ȩ��
        smtpObj.login("an1090146450@163.com", "HMIJRCNOLTPZCUNW")
        # �����˵�ַ���ռ��˵�ַ����Ϊ�б��ַ���["1XX@qq.com","2XX@qq.com"]��
        # �ʼ�����:һ����msg.as_string():�ǽ�msg(MIMEText�������MIMEMultipart����)��Ϊstr��
        smtpObj.sendmail("an1090146450@163.com", "1090146450@qq.com", msg.as_string())
        # �˳�
        smtpObj.quit()
