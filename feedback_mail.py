import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(name, contact_email, text):
    msg = MIMEMultipart()
    text = f'{text}\n\n{contact_email}'

    msg["From"] = 'CSGrenade@yandex.ru'
    msg["To"] = 'CSGrenade@yandex.ru'
    msg['Subject'] = f'{name} отправил отзыв!'
    msg.attach(
        MIMEText(text, 'plain')
    )

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.ehlo('CSGrenade@yandex.ru')
    server.login('CSGrenade@yandex.ru', 'CSGrenade2022')
    server.auth_plain()
    server.send_message(msg)
    server.quit()

    return 'OK'

