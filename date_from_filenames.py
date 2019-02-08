import os
import re
import datetime
from configuration import MODEL_PATH

date_pattern = re.compile(r'(\d{4})(\d{2})(\d{2})(\d{2})(\d{2})\.')

def getDate(filename):
    matched = date_pattern.search(filename)
    if not matched:
        return None
    y, m, d, H, M = map(int, matched.groups())
    return datetime.datetime(y, m, d, H, M)
    
def getMaxDate():
	filenames, _ = getFileDetails()
	dates = (getDate(fn) for fn in filenames)
	dates = (d for d in dates if d is not None)
	last_date = max(dates)
	last_date = last_date.strftime('%Y%m%d%H%M')
	filenames = [fn for fn in filenames if last_date in fn]
	name = MODEL_PATH + filenames[0]
	return name	

def getMinDate():
	filenames, _ = getFileDetails()
	dates = (getDate(fn) for fn in filenames)
	dates = (d for d in dates if d is not None)
	old_date = min(dates)
	old_date = old_date.strftime('%Y%m%d%H%M')
	filenames = [fn for fn in filenames if old_date in fn]
	name = MODEL_PATH + filenames[0]
	return name	

def getFileDetails():
	filenames = os.listdir(MODEL_PATH)
	return filenames, len(filenames)
	
if __name__ == '__main__':
    print(getMaxDate(), getMinDate())
