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

    def getAllCategories(self, take=999999):
        body = {
            'id': str(uuid4()),
            'method': 'get',
            'to': 'postmaster@analytics.msging.net',
            'uri': '/event-track?$take=%s' % (take),
        }

        command = self.Session.post('https://msging.net/commands', json=body)
        command = command.json()

        report = [tracking['category'] for tracking in command['resource']['items']]

        return report

    def getCustomReport(self, uri, start_date, end_date, take=999999, retry_attempts=3):
        while retry_attempts:
            try:
                body = {
                    'id': str(uuid4()),
                    'method': 'get',
                    'to': 'postmaster@analytics.msging.net',
                    'uri': '%s?startDate=%sT03%%3A00%%3A00.000Z&endDate=%sT03%%3A00%%3A00.000Z&$take=%s' %
                    (uri, start_date.strftime('%Y-%m-%d'),
                    end_date.strftime('%Y-%m-%d'), take)
                }

                command = self.Session.post(
                    'https://msging.net/commands',
                    json=body
                )

                command = command.json()
               
                return command['resource']['items']
                
            except Exception as identifier:
                print(f'Exception occurred\nWill retry: {retry_attempts}\n{identifier}\n\n{command}')

                sleep_time = [0, 10, 5, 3]
                time.sleep(sleep_time[retry_attempts])
                
                retry_attempts -= 1

