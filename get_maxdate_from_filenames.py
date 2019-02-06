import os
import re
import datetime

date_pattern = re.compile(r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})\.')

def get_date(filename):
    matched = date_pattern.search(filename)
    if not matched:
        return None
    y, m, d, H, M = map(int, matched.groups())
    return datetime.datetime(y, m, d, H, M)
    
def get_maxdate():
	filenames = os.listdir(MODEL_PATH)
	dates = (get_date(fn) for fn in filenames)
	dates = (d for d in dates if d is not None)
	last_date = max(dates)
	last_date = last_date.strftime('%Y%m%d%H%M')
	filenames = [fn for fn in filenames if last_date in fn]
	name = MODEL_PATH + filenames[0]
	return name	
