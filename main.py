import sys

from blip_report_requisitor import Requisitor
from datetime import datetime
from dateutil.relativedelta import relativedelta

import json
from google_sheets import GoogleSheets

from pprint import pprint
from random import randint

from trackings import Trackings

months = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
def getMonthFromDate(date):
    date = str(date)
    numeric_month = int(date.split('-')[1])
    return months[numeric_month-1]

def get_date_period():
    try:
        from_date = datetime.strptime(sys.argv[1], '%Y-%m-%d')
        to_date = datetime.strptime(sys.argv[2], '%Y-%m-%d')
        return (from_date, to_date)
    except:
        print("É necessário passar uma data inicial e uma data final, no formato mes/dia/ano")
        return (None, None)

spreadsheet_client = GoogleSheets().login()
spreadsheet = spreadsheet_client.open("PlanilhaTesteIntegracao")

worksheet = spreadsheet.add_worksheet("Main" + str(randint(0, 1000)), 1, 13)
spreadsheet.del_worksheet(spreadsheet.get_worksheet(0))

oneMonth = relativedelta(months=+1)

worksheet.insert_row(["Tracking"] + months)
trackings = Trackings()
trackings_names = trackings.get_all()
for tracking in trackings_names:
    begin_date, end_date = get_date_period()
    monthly_value = []

    while begin_date <= end_date:
        month = getMonthFromDate(begin_date)
        value_for_month = trackings.get_value(tracking, begin_date, begin_date + oneMonth)
        if (type(value_for_month) is not int):
            print(f'tracking {tracking} is wrong')
        else:
            monthly_value.append(value_for_month)
        begin_date += oneMonth
    worksheet.append_row([tracking] + monthly_value)
