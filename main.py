
from google_sheets import GoogleSheets
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from reports import *

from trackings import Trackings

from time import time
from datetime import datetime

from pprint import pprint

from collections import defaultdict

start_time = time()

reports_available = [
    ('Daily', DailyReport, 'google_spreadsheet'),
    ('Monthly', MonthlyReport, 'google_spreadsheet'),
    ('MAU', MAUReport, ''),
]

def display_report_list():
    reports = '\n'.join([f'\t{index+1} - {name}' for index, (name, _, _) in enumerate(reports_available)])

    print('Choose the report:')
    print(reports)

def get_report():
    report_chosen = -1
    while report_chosen not in range(len(reports_available)):
        report_chosen = int(input(': '))
        report_chosen -= 1
    
    print(f'\nYou chose the "{reports_available[report_chosen][0]}" report\n')
    return reports_available[report_chosen]

display_report_list()
report_name, report_generator, output_to = get_report()

report = report_generator()
volume = report.generate()

if output_to == 'google_spreadsheet':
    google_sheets = GoogleSheets()
    spreadsheet = google_sheets.open("PlanilhaTesteIntegracao")
    spreadsheet.values_update(report_name, params={'valueInputOption': 'RAW'}, body={'values': volume})

elapsed_time = time() - start_time
print(f'Duração: {elapsed_time/60} minutos')