__author__ = 'john.houghton'

import os
import datetime
import sys
from datetime import datetime
from datetime import timedelta

dt = sys.argv[1]
current_date = datetime.strptime(sys.argv[1], "%Y-%m-%d")
previous_date = (current_date - timedelta(1)).strftime("%Y-%m-%d")
current_dir = os.path.dirname(os.path.abspath(__file__))


cmd = 'pig -f '+current_dir +'/pig/report.target3.pig -l '+current_dir+'/log/report.target3.'+dt+'.pig -param ' \
                                                                                                 'dt='+dt+' -stop_on_failure'
print (cmd)
status = os.system(cmd)
if status > 0:
	print 'Error executing pig script'
	sys.exit(1)

