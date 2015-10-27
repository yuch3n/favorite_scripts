import smtplib
import time
import datetime

first_part = 'This is the first half ,'
second_part = 'and this is the rest of the message'
subject_start = 'Hi!'
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')

def sendemail(from_addr, to_addr_list, cc_addr_list,
              subject, message,
              login, password,
              smtpserver='mail.domain.com:25'):
    header  = 'From: %s\n' % from_addr
    header += 'To: %s\n' % ','.join(to_addr_list)
    header += 'Cc: %s\n' % ','.join(cc_addr_list)
    header += 'Subject: %s\n\n' % subject
    message = header + message

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(login,password)
    problems = server.sendmail(from_addr, to_addr_list, message)
    server.quit()
    return problems

sendemail(from_addr    = 'email@domain.com',
          to_addr_list = ['user@gmail.com'],
          cc_addr_list = [''],
          subject      = subject_start + st,
          message      = first_part + second_part,
          login        = 'email@domain.com',
          password     = 'passwork' )