import urllib.parse
from blip_report_requisitor import Requisitor
import json

class Trackings:
    def __init__(self):
        bot_credentials = json.load(open('credentials/bot.json', 'r'))
        self.requisitor = Requisitor(bot_credentials['key'])
    
    def get_all(self):
        return self.requisitor.getAllTrackingCategories()

    def get_value(self, name, begin_date, end_date):
        url = f"/event-track/{urllib.parse.quote(name)}"
        return self.requisitor.getCustomReport(url, begin_date, end_date)
