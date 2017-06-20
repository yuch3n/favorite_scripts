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
  conn = pyodbc.connect(config.VERTICA_BI_DSN, ansi = 'False', autocommit = True)
  cursor = conn.cursor()
  cursor.execute(statement)
  ret = []
  for r in cursor.fetchall():
    ret.append(r)
  conn.close()
  return [list(r) for r in ret]

results = query(     '''
with a as  (
        WITH pri as ( select a.day
                        , psm.app_id
                        , psm.video_offer_id
                        , count(1) as video_conversions
                        , -.01*sum(a.advertiser_amount) as spend
                    from analytics.actions a join
                    (select distinct video_offer_id, app_id from analytics.primary_secondary_mapping
                    where app_id is not null and item_type = 'App') psm
                    on a.offer_id = psm.video_offer_id
                    where -- last 7 days
                        a.day >= current_date -15 and a.day <= current_date - 1
                    group by 1,2,3

                    ) ,
             sec as (  select a.day ,
                        psm.video_offer_id,
                        count(1) as installs
                    from analytics.actions a join
                    analytics.primary_secondary_mapping psm
                    on (a.predecessor_offer_id = psm.video_offer_id and a.offer_id = psm.secondary_offer_id)
                    where -- last 7 days
                        a.day >= current_date -15 and a.day <= current_date - 1
                        and psm.item_type = 'App'
                        and psm.app_id is not null
                        group by 1,2
                     )

        select pri.day,
            pri.app_id as app_id ,
            pri.video_offer_id as offer_id ,
            sum(pri.video_conversions) as vid_convs ,
            round( sum(pri.spend) ,2) as spend,
            sum(sec.installs)  as installs
        from pri
        left join sec
            on pri.video_offer_id = sec.video_offer_id
            and pri.day = sec.day
        group by 1,2,3
        )
select a.day as a_day
, a.vid_convs as a_vid_convs
, a.spend as a_spend
, a.installs as a_installs
, b.day as b_day
, b.offer_id as b_offer_id
, b.vid_convs as b_vid_convs
, b.spend as b_spend
, b.installs as b_installs
FROM a a
JOIN a b on a.offer_id = b.offer_id
      and a.day = (b.day - 1)
GROUP BY 1,2,3,4,5,6,7,8,9
;
''' )

# convert results to pandas df
df = pd.DataFrame(results)
# set filename
filename = 'data_' + todays_date + '.csv'
# save pandas df as .csv
df.to_csv(filename, header=['a_day', 'a_vid_convs', 'a_spend', 'a_installs', 'b_day', 'b_offer_id', 'b_vid_convs',
                            'b_spend', 'b_installs'])

