import sys

from blip_report_requisitor import Requisitor
from datetime import datetime
from dateutil.relativedelta import relativedelta

import json
from google_sheets import GoogleSheets

from pprint import pprint
from random import randint

from trackings import Trackings
from blip_report_maker import ReportMaker

reportMaker = ReportMaker()
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

sys.exit()



trackings = Trackings()
trackings_names = trackings.get_all()



google_sheets_client = GoogleSheets()
spreadsheet_client = google_sheets_client.get()
spreadsheet = spreadsheet_client.open("PlanilhaTesteIntegracao")

# google_sheets_client.replace_worksheet(0, ("Main", 1, 13))

oneMonth = relativedelta(months=+1)

worksheet.insert_row(["Tracking"] + months)
trackings = Trackings()
trackings_names = trackings.get_all()
for tracking in trackings_names:
    begin_date, end_date = get_date_period()
    monthly_value = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while begin_date <= end_date:
        month_number, month = getMonthFromDate(begin_date)
        value_for_month = trackings.get_value(tracking, begin_date, begin_date + oneMonth)
        if (type(value_for_month) is not int):
            pprint(f'tracking {tracking} -> {value_for_month} is wrong')
        else:
            monthly_value[month_number] = value_for_month
        begin_date += oneMonth
    worksheet.append_row([tracking] + monthly_value)

wks.values_update(
'HP WPP BH!A2',
params={'valueInputOption': 'RAW'}, 
body={'values': rows})