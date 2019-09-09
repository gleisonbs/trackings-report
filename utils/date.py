
import sys
from datetime import datetime

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def get_month_list():
    return months

def get_days_list():
    return [d for d in range(1, 32)]

def get_month_from_date(date):
    month = date.month
    return (month - 1, months[month-1])

def get_day_from_date(date):
    return date.day

def get_date_range():
    try:
        from_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
        to_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')

        if to_date > datetime.now():
            to_date = datetime.now()

        return (from_date, to_date)
    except:
        year = datetime.now().year
        return (datetime(year, 1, 1), datetime.now())