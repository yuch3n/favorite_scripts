__author__ = 'john.houghton'

mport sqlite3
import pandas as pd
con = sqlite3.connect("/var/www/path/db.sqlite3")

sql_query = ''' SELECT * FROM db '''
df = pd.read_sql(sql_query, con)

df.to_csv('/home/path/file_name.csv')