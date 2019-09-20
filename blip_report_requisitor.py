from requests import Session
from functools import reduce
from uuid import uuid4
from json import dumps
import time


def percentage(part, whole):
    return round(100 * float(part) / float(whole), 2)


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

    def getCustomReport(self, uri, start_date, end_date, take=999999, retry_attempts=3):
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
                print(f'Exception occurred\nWill retry: {retry_attempts}\n{identifier}\n\n{command}')

                time.sleep(self.retry_wait)
                
                retry_attempts -= 1

