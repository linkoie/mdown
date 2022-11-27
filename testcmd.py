import sys
import os
import datetime

# command = 'df -h'
# val = os.system(command)
# print(val)

# cmd1 = sys.argv[1]
# print(cmd1)
# v = os.system(cmd1)
# print(v)

date_time = datetime.datetime.now().strftime('%Y%m%d-%H%M')
print(date_time)