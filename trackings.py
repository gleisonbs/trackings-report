import urllib.parse
from blip_report_requisitor import Requisitor
import json
import re

from ignore_trackings import trackings_to_ignore

class Trackings:
    def __init__(self):
        self.all_trackings = []
        bot_credentials = json.load(open('credentials/bot.json', 'r'))
        self.requisitor = Requisitor(bot_credentials['key'])
    
    def get_categories(self):
        return self.get_all_correct_trackings()

    def get_value(self, name, begin_date, end_date):
        url = f"/event-track/{urllib.parse.quote(name)}"
        return self.requisitor.getCustomReport(url, begin_date, end_date)

    def __get_all_trackings(self, refresh = False):
        if refresh or not self.all_trackings:
            self.all_trackings = [t for t in self.requisitor.getAllCategories() if t not in trackings_to_ignore]
        return self.all_trackings

    def is_option_tracking(self, tracking):
        return tracking.lower().endswith(' opcoes') or tracking.lower().endswith(' opçao')
        
    def is_userId_tracking(self, tracking):
        return tracking.lower().endswith(' userid')

    def is_origin_tracking(self, tracking):
        return tracking.lower().endswith(' origem')
    
    def is_content_tracking(self, tracking):
        return tracking.lower().endswith(' conteudo')

    def starts_with_id(self, tracking):
        return re.match("^([a-zA-z]{1})(\.[0-9]+)+\s+\w+", tracking)
    
    def starts_with_letter(self, tracking):
        return tracking[0].isalpha()

    def contains_brackets(self, tracking):
        return '[' in tracking

    def is_too_short(self, tracking):
        return len(tracking) < 4

    def __is_trackings_wrong(self, tracking):
        return not self.starts_with_letter(tracking) \
                or self.starts_with_id(tracking) \
                or self.contains_brackets(tracking)

    def get_all_wrong_trackings(self):
        return [tracking for tracking in self.__get_all_trackings() if self.__is_trackings_wrong(tracking)]

    def get_all_correct_trackings(self):
        return [tracking for tracking in self.__get_all_trackings() if not self.__is_trackings_wrong(tracking)]

    def get_all_exhibition_trackings(self):
        return [tracking for tracking in self.get_all_correct_trackings() if not self.is_origin_tracking(tracking) and
                                                                             not self.is_content_tracking(tracking) and
                                                                             not self.is_userId_tracking(tracking) and
                                                                             not self.is_option_tracking(tracking)]

    def getMAU(self, start_date, end_date):
        return self.requisitor.getMau(start_date, end_date)