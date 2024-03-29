from trackings import Trackings
from utils.date import get_date_range, get_month_from_date, get_months
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint
from time import sleep
from datetime import datetime
from collections import defaultdict

class MAUReport:
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
        print('Running the "MAU" report...')

        begin_date, end_date = get_date_range()
        months = get_months(begin_date.month, end_date.month)

        oneMonth = relativedelta(months = +1)
        oneDay = relativedelta(days = +1)
        for month_name, month_number in months:
            
            total_MAU = self.trackings.getMAU(begin_date, (begin_date + oneMonth) - oneDay)
            begin_date += oneMonth

            self.rows.append([month_name] + [total_MAU])

            print(f'{month_name}: {total_MAU}')
        
        self.rows = self.add_header(self.rows)
        return self.rows