from trackings import Trackings
from utils.date import get_date_range, get_day_from_date, get_month_from_date, get_months, get_days_list
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint

from collections import defaultdict
from datetime import datetime

class ListAllTrackings:
    def __init__(self):
        self.rows = []
        self.trackings = Trackings()

    def generate(self):
        print('Running the "Tracking list" report...\n')

        all_trackings = self.trackings.get_all_trackings()

        return all_trackings
        