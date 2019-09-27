from trackings import Trackings
from utils.date import get_date_range, get_month_from_date, get_months
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
                continue

            storageDate = datetime.strptime(t['storageDate'][:10], '%Y-%m-%d')
            report[(storageDate.year, storageDate.month)] += t['count']
        return dict(report)
    
    def add_header(self, rows):
        updated_at = f'Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        months = [''] + [month for month, _ in get_months()]

        rows.insert(0, months)
        rows.insert(0, [updated_at])
        return rows

    def print_bad_trackings(self):
        print('\n\nTrackings que não são de exibição:\n')
        print(self.bad_trackings)

    def get_monthly_count(self, grouped_by_months):
        monthly_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for (year, month) in grouped_by_months:
            monthly_values[month-1] = grouped_by_months[(year, month)]
        return monthly_values

    def is_valid_tracking(self, tracking, grouped_by_months):
        if type(grouped_by_months) is str and grouped_by_months.startswith('invalid'):
            self.bad_trackings.append(f'{tracking} -> action: {grouped_by_months.split(":")[1]}')
            return False
        return True

    def generate(self):
        print('Running the "Monthy" report...')
        trackings_names = self.trackings.get_all_exhibition_trackings()

        start_date, final_date = get_date_range()
        for tracking in trackings_names:
            print(tracking)
            begin_date, end_date = start_date, final_date
            
            tracking_totals = self.trackings.get_value(tracking, begin_date, end_date)
            grouped_by_months = self.group_by_month(tracking_totals)

            if not self.is_valid_tracking(tracking, grouped_by_months):
                continue
            
            monthly_values = self.get_monthly_count(grouped_by_months)

            self.rows.append([tracking] + monthly_values)

        self.print_bad_trackings()
        self.rows = self.add_header(self.rows)

        return self.rows
