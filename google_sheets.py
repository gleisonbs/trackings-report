import gspread
from oauth2client.service_account import ServiceAccountCredentials

class GoogleSheets:
    def __init__(self):
        self.path_credentials = 'credentials/googlesheets.json'
        self.scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        
        credentials = ServiceAccountCredentials.from_json_keyfile_name(self.path_credentials, self.scope)
        self.spreadsheet = gspread.authorize(credentials)
    
    def open(self, spreadsheet_name):
        return self.spreadsheet.open(spreadsheet_name)
    
    def replace_worksheet(self, index, new_worksheet):
        worksheet_to_delete = self.spreadsheet.get_worksheet(0)
        worksheet_to_delete.update_title("Deleting")

        worksheet = spreadsheet.add_worksheet(*new_worksheet)
        self.spreadsheet.del_worksheet(worksheet_to_delete)