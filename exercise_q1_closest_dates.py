import sys
from datetime import datetime

def validate_date(date_str):
    try:
        date = datetime.strptime(date_str, "%Y%m%d")
        return date >= datetime(1600, 1, 1)
    except ValueError:
        return False

def main():
    dates = []
    for line in sys.stdin:
        if validate_date(line):
            dates.append(datetime.strptime(line, "%Y%m%d"))
    legal_dates = sorted(dates)

    if len(legal_dates) < 2:
        print(-1)
        return        
    min_difference = (legal_dates[1] - legal_dates[0]).days

    for i in range(2, len(legal_dates)):
        difference = (legal_dates[i] - legal_dates[i - 1]).days
        min_difference = min(min_difference, difference)

    print(min_difference)
    return

if __name__ == "__main__":
    main()