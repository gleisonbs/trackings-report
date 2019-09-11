
from google_sheets import GoogleSheets
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from reports import MonthlyReport
from reports import DailyReport

from trackings import Trackings

from time import time

# reportMaker = ReportMaker()
# all_correct_trackings = reportMaker.get_all_correct_trackings()
# t = Trackings()
# with open('correct_trackings.txt', 'w') as correct_trackings:
#     all_correct_trackings = reportMaker.get_all_correct_trackings()

#     for i in range(5):
#         print(t.get_value(all_correct_trackings[i], datetime(2019, 5, 5), datetime(2019, 6, 6)))
#         print('\n')

#     correct_trackings.write(f"Correct trackings: {len(all_correct_trackings)}\n")
#     correct_trackings.write('\n'.join(all_correct_trackings))

# with open('wrong_trackings.txt', 'w') as wrong_trackings:
#     all_wrong_trackings = reportMaker.get_all_wrong_trackings()

#     wrong_trackings.write(f"Wrong trackings: {len(all_wrong_trackings)}\n")
#     wrong_trackings.write('\n'.join(all_wrong_trackings))

start_time = time()

google_sheets = GoogleSheets()
spreadsheet = google_sheets.open("PlanilhaTesteIntegracao")

monthlyReport = MonthlyReport()
monthly_tracking_volume = monthlyReport.generate()
spreadsheet.values_update('Monthly', params={'valueInputOption': 'RAW'}, body={'values': monthly_tracking_volume})

# dailyReport = DailyReport()
# daily_tracking_volume = dailyReport.generate()
# spreadsheet.values_update('Daily', params={'valueInputOption': 'RAW'}, body={'values': daily_tracking_volume})

elapsed_time = time() - start_time
print(f'Duração: {elapsed_time/60} minutos')