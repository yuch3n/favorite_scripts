__author__ = 'john.houghton'

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import time
import datetime

ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

MAIL_SERVER = 'mail.domain.com'
SENDER_EMAIL = 'email@domain.com'
SENDER_USER = 'email@domain.com'
SENDER_PASSWORD = 'password'


def send_mail(to_email, subject, text, file_path_list):
    msg = MIMEMultipart()

    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    for f in file_path_list:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(open(f, 'rb').read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' \
                        % os.path.basename(f))
        msg.attach(part)

    mail_server = smtplib.SMTP(MAIL_SERVER)
    mail_server.login(SENDER_USER, SENDER_PASSWORD)
    mail_server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
    mail_server.close()

import datetime
mdate = "2016-03-19"
rdate = st
mdate1 = datetime.datetime.strptime(mdate, "%Y-%m-%d").date()
rdate1 = datetime.datetime.strptime(rdate, "%Y-%m-%d").date()
delta =  (mdate1 - rdate1).days
delta = str(delta)

if __name__ == "__main__":
    to_email = 'send_to_email@gmail.com'
    subject_start = 'Updated Wedding RSVPS for '
    subject = 'Updated RSVPs @ ' + st + '. Only ' + delta + ' days left!'
    text1 = 'Here are the most updated wedding RSVPs from the system as of '
    text = text1 + st
    file_path_list = ['/path/file.csv']
    text = text1 + st
    file_path_list = ['/path/file.csv']

    send_mail(to_email, subject, text, file_path_list)