
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
    while True:
        try:
            #from_date = datetime.strptime(sys.argv[1], '%Y-%m-%d').date()

            current_year = datetime.now().date().year
            start_date = datetime(current_year, 1, 1).date()
            new_date = input(f'Start date (press enter to use {start_date.strftime("%Y-%m-%d")}): ')
            if new_date:
                start_date = datetime.strptime(new_date, "%Y-%m-%d")

            to_date = datetime.now().date()
            new_date = input(f'End date (press enter to use {to_date.strftime("%Y-%m-%d")}): ')
            if new_date:
                to_date = datetime.strptime(new_date, "%Y-%m-%d")
            
            if to_date > datetime.now().date():
                to_date = datetime.now().date()

            return (start_date, to_date)
        except Exception as e:
            print(f'\n\n{e}\n\n')