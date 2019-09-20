
import sys
from datetime import datetime

months = [('Janeiro', 1), ('Fevereiro', 2), ('Março', 3), ('Abril', 4), ('Maio', 5), ('Junho', 6), ('Julho', 7), ('Agosto', 8), ('Setembro', 9), ('Outubro', 10), ('Novembro', 11), ('Dezembro', 12)]

def get_months(from_month=1, to_month=12):
    return months[from_month-1:to_month]

def get_days_list():
    return [d for d in range(1, 32)]

def get_month_from_date(date):
    month = date.month
    return (month - 1, months[month-1])

def get_day_from_date(date):
    return date.day

def get_date_range():
    try:
        if len(sys.argv) >= 2:
            from_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')

        if len(sys.argv) >= 3:
            to_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')

        if to_date > datetime.now():
            to_date = datetime.now()

        return (from_date, to_date)
    except:
        year = datetime.now().year
        return (datetime(year, 1, 1), datetime.now())