import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


def send_email(config_dict, data):

    sender_email = config_dict.sender_email
    password = config_dict.sender_password
    receiver_email = config_dict.receiver_email

    message = MIMEMultipart("alternative")
    message["Subject"] = "New Job Postings"
    message["From"] = sender_email
    message["To"] = receiver_email

    # plain-text version of message
    text = ""
    for i in range(len(data)):
        text += """\
            {0}
            {1}
            {2}
            {3}\n\n\n
        """.format(data.title, data.company, data.location, data.url)

    # # HTML version of message
    # html = """\
    #     <html>
    #         <body>
    # """
    # for i in range(len(data)):
    #     html += """\
    #         <p>{0}<br>
    #             {1}<br>
    #             <a href="{http://www.realpython.com}">Real Python</a> 
    #             has many great tutorials.
    #         </p>
    #     </body>
    # </html>
    # """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    # part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )