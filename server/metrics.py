import json
import glob
import os
import re
import sys
import time

# run with 0 as an argument to parse all files.
parse_from_unix_date = float(sys.argv[1])

log_file_names= glob.glob('../logs/**/*.json', recursive=True)
with open('../logs/log_metrics.csv','w') as output_file:
	for lfn in log_file_names:
		log_os_time = os.path.getmtime(lfn)
		if log_os_time > parse_from_unix_date:
			with open(lfn,'r') as lf:
				lfc = lf.read()
				inactivity_match = re.search(r'\|inactive\|([^ ]+?) reconnected and has \d+ seconds left.',lfc)
				if inactivity_match:
					output_file.write('stamp,user,room\n')
					user = inactivity_match.group(1)
					room_id_match = re.search(r'"roomid":"(.+?)"',lfc[inactivity_match.end(1):])
					room_id = room_id_match.group(1)
					output_file.write(f'{log_os_time:.2f},{user},{room_id}\n')


print( str(time.time()))




