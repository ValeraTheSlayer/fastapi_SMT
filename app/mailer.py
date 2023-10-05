import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging
import os

def send_email(to, subject, message):
    """
    Отправляет электронное письмо.

    :param to: Получатель письма
    :param subject: Тема письма
    :param message: Текст письма
    :return: True, если письмо успешно отправлено. В противном случае, False.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = os.environ.get('SMTP_EMAIL')
        msg['To'] = to
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(os.environ.get('SMTP_SERVER', 'smtp.mailgun.org'), int(os.environ.get('SMTP_PORT', 587)))
        server.starttls()

        server.login(msg['From'], os.environ.get('SMTP_PASSWORD'))
        server.sendmail(os.environ.get('SMTP_EMAIL'), to, msg.as_string())
        server.quit()

        logging.info(f"Successfully sent email to {to}")

        return True

    except Exception as e:
        logging.error(f"Failed to send email: {str(e)}")
        return False
