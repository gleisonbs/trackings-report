from blip_report_requisitor import Requisitor
import re
import json

class ReportMaker:
    def __init__(self):
        self.all_trackings = []
        bot_credentials = json.load(open('credentials/bot.json', 'r'))
        self.requisitor = Requisitor(bot_credentials['key'])

    def __get_all_trackings(self, refresh = False):

        if refresh or not self.all_trackings:
            self.all_trackings = self.requisitor.getAllCategories()
        return self.all_trackings

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
                or self.contains_brackets(tracking) \
                or self.is_too_short(tracking)

    def get_all_wrong_trackings(self):
        return [tracking for tracking in self.__get_all_trackings() if self.__is_trackings_wrong(tracking)]

    def get_all_correct_trackings(self):
        return [tracking for tracking in self.__get_all_trackings() if not self.__is_trackings_wrong(tracking)]
        