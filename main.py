
from google_sheets import GoogleSheets
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from reports import MonthlyReport
from reports import DailyReport

from trackings import Trackings

from time import time
from datetime import datetime

from pprint import pprint

from collections import defaultdict

start_time = time()

google_sheets = GoogleSheets()
spreadsheet = google_sheets.open("PlanilhaTesteIntegracao")

# monthlyReport = MonthlyReport()
# monthly_tracking_volume = monthlyReport.generate()
# spreadsheet.values_update('Monthly', params={'valueInputOption': 'RAW'}, body={'values': monthly_tracking_volume})

dailyReport = DailyReport()
daily_tracking_volume = dailyReport.generate()
spreadsheet.values_update('Daily', params={'valueInputOption': 'RAW'}, body={'values': daily_tracking_volume})

elapsed_time = time() - start_time
print(f'Duração: {elapsed_time/60} minutos')