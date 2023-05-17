import datetime
import sys

previous_date = None
for i, line in enumerate(sys.stdin):
    date_str = line.strip()
    try:
        date = datetime.datetime.strptime(date_str, "%d%m%Y")
    except ValueError:
        print(f"Line {i+1}: Illegal")
        previous_date = None
        continue
    if date.year <= 1600:
        print(f"Line {i+1}: Illegal")
        previous_date = None
        continue

    if previous_date != None and date < previous_date:
        print(f"Line {i+1}: Older")
    previous_date = date