import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from django.conf import settings


# 随机生成6位数字验证码
def random_code():
    code = ""
    digit = [str(i) for i in range(10)]
    for j in range(6):
        code += random.choice(digit)
    return code


def send_email(receiver):
    smtp_server = settings.EMAIL_SMTP_SERVER  # 网易邮箱的SMTP服务器地址
    smtp_port = settings.EMAIL_SMTP_PORT  # 默认端口为25
    sender = settings.EMAIL_SENDER  # 发件人邮箱
    password = settings.EMAIL_PASSWORD  # 发件人邮箱密码
    code = random_code()

    # 邮件内容
    subject = '验证码'
    body = '你的验证码是:{}'.format(code)

    msg = MIMEText(body, 'plain', 'utf-8')
    msg['From'] = Header(sender)
    msg['To'] = Header(receiver)
    msg['Subject'] = Header(subject, 'utf-8')

    try:
        # 连接SMTP服务器
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.login(sender, password)  # 登录邮箱账号

        # 发送邮件
        server.sendmail(sender, receiver, msg.as_string())
        print('邮件发送成功！')

    except smtplib.SMTPException as e:
        print('邮件发送失败：', str(e))

    finally:
        server.quit()  # 关闭连接

    return 0


if __name__ == '__main__':
    send_email("1727693015@qq.com")
