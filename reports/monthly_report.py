from trackings import Trackings
from utils.date import get_date_range, get_month_from_date, get_month_list
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint
from time import sleep

class MonthlyReport:
    def __init__(self):
        self.rows = []
        self.trackings = Trackings()

    def get_tracking_count(self, tracking, from_date, to_date):
        return self.trackings.get_value(tracking, from_date, to_date)

    def generate(self):
        trackings_names = self.trackings.get_all_view_trackings()

        oneMonth = relativedelta(months=+1)
        # counter = 0
        for tracking in trackings_names:
            sleep(2) # delay so we wont flood the api
            begin_date, end_date = get_date_range()
            monthly_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

            while begin_date <= end_date:
                month_number, _ = get_month_from_date(begin_date)
                monthly_total = self.get_tracking_count(tracking, begin_date, begin_date + oneMonth)

                if (type(monthly_total) is not int):
                    log_error(f'tracking {tracking} -> {monthly_total} is wrong')
                else:
                    monthly_value[month_number] = monthly_total

                begin_date += oneMonth
            self.rows.append([tracking] + monthly_value)
            # if (counter > 50):
            #     break
            # counter = counter + 1

        months = [''] + get_month_list()
        self.rows.insert(0, months)
        return self.rows
