###################################################################################
#####                                                                         #####
##### Code originally from https://github.com/chr0m1ng/blip-report-requisitor #####
#####                                                                         #####
###################################################################################

from requests import Session
from functools import reduce
from uuid import uuid4
from json import dumps
import time
from datetime import datetime

class Requisitor(object):

    def __init__(self, authorization=''):
        if authorization[0:3].lower() != 'key':
            authorization = 'Key %s' % authorization
        self.Session = Session()
        self.Session.headers.update({'Authorization': authorization})
        self.retry_wait = 10 # in seconds

    def getAllCategories(self, take=999999):
        body = {
            'id': str(uuid4()),
            'method': 'get',
            'to': 'postmaster@analytics.msging.net',
            'uri': f'/event-track?$take={take}'
        }

        command = self.Session.post('https://msging.net/commands', json=body)
        command = command.json()

        report = [tracking['category'] for tracking in command['resource']['items']]

        return report

    def getCustomReport(self, uri, start_date, end_date, take=999999, retry_attempts=5):
        start_date = start_date.strftime('%Y-%m-%d')
        end_date = end_date.strftime('%Y-%m-%d')

        while retry_attempts:
            try:
                body = {
                    'id': str(uuid4()),
                    'method': 'get',
                    'to': 'postmaster@analytics.msging.net',
                    'uri': f'{uri}?startDate={start_date}T03%3A00%3A00.000Z&endDate={end_date}T03%3A00%3A00.000Z&$take={take}'
                }

                command = self.Session.post(
                    'https://msging.net/commands',
                    json=body
                )

                command = command.json()
               
                return command['resource']['items']
                
            except Exception as identifier:
                print(f'Exception occurred\nI will retry {retry_attempts} more times\n{identifier}\n\n{command}')

                time.sleep(self.retry_wait)
                
                retry_attempts -= 1

    def getBotConfiguration(self):
        body = {
            'id': str(uuid4()),
            'method': 'get',
            'uri': '/account'
        }
        command = self.Session.post('https://msging.net/commands', json=body)
        command = command.json()

        return command['resource']

    def getAllMau(self):
        bot_config = self.getBotConfiguration()
        creation_datetime = datetime.strptime(bot_config['creationDate'], '%Y-%m-%dT%H:%M:%S.%fZ')
        return self.getMau(creation_datetime, datetime.now())

    def getMau(self, start_date, end_date):
        mau_uri = f'/metrics/active-identity/NI'
        return self.getCustomReport(mau_uri, start_date, end_date)

