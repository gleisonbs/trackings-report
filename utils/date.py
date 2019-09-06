
import sys
from datetime import datetime

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

def get_month_list():
    return months

def get_month_from_date(date):
    date = str(date)
    numeric_month = int(date.split('-')[1])
    return (numeric_month - 1, months[numeric_month-1])

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