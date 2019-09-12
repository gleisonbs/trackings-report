from trackings import Trackings
from utils.date import get_date_range, get_day_from_date, get_month_from_date, get_month_list, get_days_list
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

    def get_tracking_count(self, tracking, from_date, to_date):
        return self.trackings.get_value(tracking, from_date, to_date)

    def generate(self):
        trackings_names = self.trackings.get_all_view_trackings()

        begin_date, end_date = get_date_range()
        current_month = 1
        for month_name in get_month_list():
            self.rows.append([month_name] + ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''])
            
            for tracking in trackings_names[:15]:
                print(f'{month_name}: {tracking}')
                daily_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                tracking_totals = self.get_tracking_count(tracking, begin_date, end_date)
                group_by_days = self.group_by_days(tracking_totals)

                if type(group_by_days) is str and group_by_days.startswith('invalid'):
                    self.bad_trackings.append(f'{tracking} -> action: {group_by_days.split(":")[1]}')
                    continue
            
                for (year, _, day) in group_by_days:
                    if (year, current_month, day) in group_by_days:                    
                        daily_values[day-1] = group_by_days[(year, current_month, day)]
                    else:
                        daily_values[day-1] = 0

                self.rows.append([tracking] + daily_values)
            self.rows.append([])

            current_month += 1

        print('\n\nTrackings que não são de exibição:\n')
        print(self.bad_trackings)
            
        days = [''] + get_days_list()
        self.rows.insert(0, days)

        updated_at = f'Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        self.rows.insert(0, [updated_at])

        return self.rows