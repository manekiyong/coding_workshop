import sys
from bisect import bisect
from datetime import datetime

def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y%m%d")
        return date >= datetime(1600, 1, 1), date
    except ValueError:
        return False, None

def abs_date_diff(date1, date2):
    diff = (date1-date2).days
    return abs(diff)

dates = sys.stdin.readlines()
legal_dates = []
min_diff = 4000000
print(min_diff)
valid, date = validate_date(dates[0].strip())
if valid:
    legal_dates.append(date)

for i, line in enumerate(dates[1:]):
    date_str = line.strip()
    valid, date = validate_date(date_str)
    if valid:
        idx = bisect(legal_dates, date)
        legal_dates.insert(idx, date)
        if len(legal_dates)>1:
            if idx == 0: # if first element
                new_min_diff = min(min_diff, abs_date_diff(date,legal_dates[idx+1]))
            elif idx == len(legal_dates)-1: # if last element
                new_min_diff = min(min_diff, abs_date_diff(legal_dates[idx-1], date))
            else: #if anything in between
                new_min_diff = min(min_diff, abs_date_diff(legal_dates[idx-1], date), abs_date_diff(legal_dates[idx+1], date))
            if new_min_diff < min_diff:
                print(new_min_diff)
                min_diff = new_min_diff
                               