from trackings import Trackings
from utils.date import get_date_range, get_month_from_date, get_months
from utils.logger import log_error
from dateutil.relativedelta import relativedelta

from pprint import pprint
from time import sleep
from datetime import datetime
from collections import defaultdict

import sys

class NPSReport:
    def __init__(self):
        self.rows = []
        self.trackings = Trackings()
        self.bad_trackings = []
    
    def group_by_rate_and_date(self, trackings):
        ratings = {}
        for t in trackings:
            date = t['storageDate'][:10]
            nota, feedback = t['action'].split(' ', 1)
            nota = int(nota)
            # year, month, day = 
            if date not in ratings:
                ratings[date] = [[], [], [], [], [], [], [], [], [], [], []]
            ratings[date][nota].append(feedback.replace('\n', ' '))
        return ratings

    def make_feedback_matrix(self, feedbacks):
        rows = []
        for date in sorted(feedbacks):
            rows.append(['', '', '', '', '', '', '', '', '', '', '', ''])
            rows.append([date, '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
            feedback_list = feedbacks[date]
            while any(feedback_list):
                notas = ['']
                for i in range(11):
                    if feedback_list[i]:
                        notas.append(feedback_list[i].pop(0))
                    else:
                        notas.append('')
                rows.append(notas)
        return rows

    def generate(self):
        print('Running the "NPS" report...')
        tracking = 'Nps pesquisa motivo'

        begin_date, end_date = get_date_range()
            
        nps_tracking = self.trackings.get_value(tracking, begin_date, end_date)
        ratings = self.group_by_rate_and_date(nps_tracking)

        feedback_messages = self.make_feedback_matrix(ratings)

        updated_at = f'Atualizado em: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'
        ratings_headers = [updated_at, '', '', '', '', '', '', '', '', '', '', '']

        self.rows.append(ratings_headers)
        self.rows.extend(feedback_messages)

        return self.rows
