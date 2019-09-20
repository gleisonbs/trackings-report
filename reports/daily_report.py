from trackings import Trackings
from utils.date import get_date_range, get_day_from_date, get_month_from_date, get_months, get_days_list
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint

from collections import defaultdict
from datetime import datetime

class DailyReport:
    def __init__(self):
        self.rows = []
        self.trackings = Trackings()
        self.bad_trackings = []
    
    def group_by_days(self, trackings):
        report = defaultdict(int)
        for t in trackings:
            if t['action'].lower() != 'exibicao':
                return f'invalid:{t["action"]}'

            storageDate = datetime.strptime(t['storageDate'][:10], '%Y-%m-%d')
            report[(storageDate.year, storageDate.month, storageDate.day)] += t['count']
        return dict(report)

    def get_daily_count(self, grouped_by_days, current_month):
        daily_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for (year, _, day) in grouped_by_days:
            if (year, current_month, day) in grouped_by_days:                    
                daily_values[day-1] = grouped_by_days[(year, current_month, day)]
            else:
                daily_values[day-1] = 0
        return daily_values

    def is_valid_tracking(self, tracking, grouped_by_days):
        if type(grouped_by_days) is str and grouped_by_days.startswith('invalid'):
            self.bad_trackings.append(f'{tracking} -> action: {grouped_by_days.split(":")[1]}')
            return False
        return True

    def add_header(self, rows):
        updated_at = f'Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        days = ['Dias:'] + get_days_list()
        rows.insert(0, days)
        rows.insert(0, [updated_at])
        return rows

    def print_bad_trackings(self):
        print('\n\nTrackings que não são de exibição:\n')
        print(self.bad_trackings)

    def generate(self):
        print('Running the "Daily" report...')
        trackings_names = self.trackings.get_all_exhibition_trackings()

        begin_date, end_date = get_date_range()
        months = get_months(begin_date.month, end_date.month)

        for month_name, month_number in months:
            self.rows.append([month_name] + ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
            
            print(f'{month_name}')
            for tracking in trackings_names:
                print(f'\t{tracking}')
                
                tracking_totals = self.trackings.get_value(tracking, begin_date, end_date)
                grouped_by_days = self.group_by_days(tracking_totals)

                if not self.is_valid_tracking(tracking, grouped_by_days):
                    continue

                daily_values = self.get_daily_count(grouped_by_days, month_number)

                self.rows.append([tracking] + daily_values)
            self.rows.append([])
            
        self.rows = self.add_header(self.rows)
        self.print_bad_trackings()

        return self.rows