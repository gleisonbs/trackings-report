import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheets:
    def __init__(self):
        self.path_credentials = 'credentials/googlesheets.json'
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        self.spreadsheet = None
    
    def login(self):
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.path_credentials, self.scope)
        self.spreadsheet = gspread.authorize(credentials)
        return self.spreadsheet
    