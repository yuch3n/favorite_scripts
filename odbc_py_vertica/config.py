ACCESS_KEY = 'AKIAIEFOIHJCCCWIR3UQ'
SECRET_KEY = '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'

VERTICA_DSN = 'DSN=VerticaDSN; UID=dbadmin; PWD=TJ4ever!'
VERTICA_DSN_PROD = 'DSN=ProdVerticaDSN; UID=dbadmin; PWD=TJ4ever!'
VERTICA_BI_DSN = 'DSN=vertica; UID=bi; PWD=tap1234!'
VERTICA_DSN_INTUIT = 'DSN=intuit-vertica; UID=jhoughton; PWD=InfinitePizza1'
RDS_SCHEMA = 'analytics'

MYSQL_HOST = 'tapjoy-db-rds-replica2.cck8zbm50hdd.us-east-1.rds.amazonaws.com'
MYSQL_PORT = 3306
MYSQL_USER = 'tapjoy'
MYSQL_PASSWORD = 'xatrugAxu6'
MYSQL_DATABASE = 'tapjoy_db'

MYSQL_CONN = "DRIVER={MySQL}; PORT=%d; SERVER=%s;DATABASE=%s; UID=%s; PASSWORD=%s;OPTION=3;" % (MYSQL_PORT, MYSQL_HOST, MYSQL_DATABASE, MYSQL_USER, MYSQL_PASSWORD)

