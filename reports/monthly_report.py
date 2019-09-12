from trackings import Trackings
from utils.date import get_date_range, get_month_from_date, get_month_list
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint
from time import sleep
from datetime import datetime
from collections import defaultdict

class MonthlyReport:
    def __init__(self):
        self.rows = []
        self.trackings = Trackings()
        self.bad_trackings = []

        
    def group_by_month(self, trackings):
        report = defaultdict(int)
        for t in trackings:

            if t['action'].lower() != 'exibicao':
                return f'invalid:{t["action"]}'

            storageDate = datetime.strptime(t['storageDate'][:10], '%Y-%m-%d')
            report[(storageDate.year, storageDate.month)] += t['count']
        return dict(report)

    def get_tracking_count(self, tracking, from_date, to_date):
        return self.trackings.get_value(tracking, from_date, to_date)

    def generate(self):
        trackings_names = self.trackings.get_all_view_trackings()

        for tracking in trackings_names:
            #print(f'\n{tracking}')
            begin_date, end_date = get_date_range()
            monthly_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            tracking_totals = self.get_tracking_count(tracking, begin_date, end_date)
            grouped_by_months = self.group_by_month(tracking_totals)

            if type(grouped_by_months) is str and grouped_by_months.startswith('invalid'):
                self.bad_trackings.append(f'{tracking} -> action: {grouped_by_months.split(":")[1]}')
                continue
            
            for (year, month) in grouped_by_months:
                monthly_values[month-1] = grouped_by_months[(year, month)]

            self.rows.append([tracking] + monthly_values)

        print('\n\nTrackings que não são de exibição:\n')
        print(self.bad_trackings)
        
        months = [''] + get_month_list()
        self.rows.insert(0, months)

        updated_at = f'Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        self.rows.insert(0, [updated_at])
        return self.rows
