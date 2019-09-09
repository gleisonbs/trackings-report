from trackings import Trackings
from utils.date import get_date_range, get_day_from_date, get_month_from_date, get_month_list, get_days_list
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint
from time import sleep

class DailyReport:
    def __init__(self):
        self.rows = []
        self.trackings = Trackings()

    def get_tracking_count(self, tracking, from_date, to_date):
        return self.trackings.get_value(tracking, from_date, to_date)

    def generate(self):
        trackings_names = ['Cliente nextel', 'Codigo de barras gerado'] # self.trackings.get_all_view_trackings()

        begin_date, end_date = get_date_range()
        for month in get_month_list():
            self.rows.append([month])
            
            for tracking in trackings_names:
                sleep(1)
                daily_values = self.get_tracking_values_in_month(tracking, begin_date)
                self.rows.append(daily_values)

            oneMonth = relativedelta(months=1)
            begin_date += oneMonth
            if (begin_date > end_date):
                break

        days = [''] + get_days_list()
        self.rows.insert(0, days)
        return self.rows

    def get_tracking_values_in_month(self, tracking, date):
        daily_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        oneDay = relativedelta(days=+1)
        while not self.next_day_is_next_month(date):
            
            day_total = self.get_tracking_count(tracking, date, date + oneDay)

            if (type(day_total) is not int):
                log_error(f'tracking {tracking} -> {day_total} is wrong')
            else:
                daily_values[date.day - 1] = day_total

            date += oneDay

        return [tracking] + daily_values

    def next_day_is_next_month(self, date):
        oneDay = relativedelta(days=+1)
        return date.month != (date - oneDay).month and date.year == (date - oneDay).year

# print('\t\t' + begin_date.strftime("%m/%d/%Y"))
