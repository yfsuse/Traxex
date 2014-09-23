#! /usr/bin/env python
#coding : utf-8

__author__ = 'jeff.yu'


import smtplib
import time
from email.message import Message
from time import sleep
import email.utils


def send_mail(subject, content):

    smtpserver = 'smtp.gmail.com'
    username = 'yfsuse@gmail.com'
    password = 'bmeB500!'

    from_addr = 'yfsuse@gmail.com'
    to_addr = 'jeff.yu@ndpmedia.com'

    mailtime = email.utils.formatdate(time.time(), True)

    message = Message()
    message['Subject'] = subject
    message['From'] = from_addr
    message['To'] = to_addr

    mailcontent = "\nQuery Time: {0}\n\n{1}\n\n".format(mailtime, content)

    message.set_payload(mailcontent)
    msg = message.as_string()

    sm = smtplib.SMTP(smtpserver, port=587, timeout=20)
    sm.set_debuglevel(1)
    sm.ehlo()
    sm.starttls()
    sm.ehlo()
    sm.login(username, password)

    sm.sendmail(from_addr, to_addr, msg)
    sleep(5)
    sm.quit()


if __name__ == "__main__":
    send_mail("mail test third", "hello\nworld\n")