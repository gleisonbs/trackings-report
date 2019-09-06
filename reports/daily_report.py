from trackings import Trackings
from utils.date import get_date_range, get_month_from_date, get_month_list
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
        self.rows = [[1, 2, 3], 
                     ['a', 'b', 'c']]
        return self.rows
