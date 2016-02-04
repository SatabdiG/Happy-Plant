#!/usr/bin/env python
import smtplib
from email.mime.text import MIMEText

USERNAME = "happy.plantv2.0@gmail.com"
PASSWORD = "happyplant2"
MAILTO  = "satabdi.ganguly89@gmail.com"

msg = MIMEText('This is the body of the email')
msg['Subject'] = 'The email subject'
msg['From'] = USERNAME
msg['To'] = MAILTO

server = smtplib.SMTP('smtp.gmail.com',587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(USERNAME,PASSWORD)
server.sendmail(USERNAME, MAILTO, msg.as_string())
server.quit()
