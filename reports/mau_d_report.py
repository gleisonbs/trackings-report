from trackings import Trackings
from utils.date import get_date_range, get_month_from_date, get_months
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint
from time import sleep
from datetime import datetime
from collections import defaultdict

class MAUDailyReport:
    def __init__(self):
        self.trackings = Trackings()
        self.rows = []

    def add_header(self, rows):
        updated_at = f'Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        empty_line = []
        rows.insert(0, empty_line)
        rows.insert(0, [updated_at])
        return rows

    def generate(self):
        print('Running the "MAU" report from {begin_date} to {end_date}\n')

        begin_date, end_date = get_date_range()

        oneDay = relativedelta(days = +1)
        while begin_date <= end_date and begin_date <= datetime.now().date():
            
            total_MAU = self.trackings.getMAU(begin_date, begin_date)
            
            self.rows.append([begin_date.strftime("%d/%m/%Y")] + [total_MAU])
            print(f'{begin_date}: {total_MAU}')

            begin_date += oneDay
        
        self.rows = self.add_header(self.rows)
        return self.rows

        