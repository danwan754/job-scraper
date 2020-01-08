import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(config_dict, data):

    sender_email = config_dict['sender_email']
    password = config_dict['sender_password']
    receiver_email = config_dict['receiver_email']
    port = 465
    smtp_server = "smtp.gmail.com"

    # plain-text version of message
    message = ""
    for i in range(len(data)):
        message += "{0}\n{1}\n{2}\n{3}\n\n\n"\
        .format(data[i]['title'], data[i]['company'], data[i]['location'], data[i]['url'])

    # # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
