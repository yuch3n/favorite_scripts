import pandas as pd
import os
import smtplib
import pyodbc
import config
import os
import time
import datetime

ts = time.time()
todays_date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')

os.environ['VERTICAINI']='/etc/odbc.ini'

def query(statement):
 # conn = pyodbc.connect(config.VERTICA_DSN_PROD, ansi = 'False', autocommit = True)
  conn = pyodbc.connect(config.VERTICA_DSN_INTUIT, ansi = 'False', autocommit = True)
  cursor = conn.cursor()
  cursor.execute(statement)
  ret = []
  for r in cursor.fetchall():
    ret.append(r)
  conn.close()
  return [list(r) for r in ret]

results = query(     '''
select * from SECURE_WS.DND_DR_TTO_LAUNCH_TY16_V4 limit 10 ;
''' )

# convert results to pandas df
df = pd.DataFrame(results)
# set filename
filename = 'data_' + todays_date + '.csv'
# save pandas df as .csv
df.to_csv(filename, header=['a_day', 'a_vid_convs', 'a_spend', 'a_installs', 'b_day', 'b_offer_id', 'b_vid_convs',
                            'b_spend', 'b_installs'])

