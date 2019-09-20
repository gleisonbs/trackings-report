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

    def generate(self):
        print('Running the "MAU" report...')

        start_date, end_date = get_date_range()

        total_MAU = self.trackings.getMAU(start_date, end_date)

        print(total_MAU)
        return total_MAU