import smtplib

from email.mime.text import MIMEText
from email_validator import validate_email, EmailNotValidError

from environs import Env


def check_email(email: str) -> bool:
    try:
        v = validate_email(email)
        email = v['email']
        return True
    except EmailNotValidError:
        return False
    

async def send_email(getter, number, path=None):

    env = Env()
    env.read_env(path)


    email_sender = 'pavelukolov007@mail.ru'

    smtp_server = smtplib.SMTP('smtp.mail.ru', 587) #465 587 993
    smtp_server.starttls()

    msg = MIMEText(f'Вас приветствует PFL! Ваш одноразовый код для входа: {number}')

    smtp_server.login(email_sender, env('PASSWORD'))
    smtp_server.sendmail(email_sender, getter, msg.as_string())
    
    smtp_server.quit()

