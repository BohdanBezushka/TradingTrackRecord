# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

TRADINGTRACKRECORD = Credentials.from_service_account_file("tradingtrackrecord.json")
SCOPED_TRADINGTRACKRECORD = TRADINGTRACKRECORD.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_TRADINGTRACKRECORD)
SHEET = GSPREAD_CLIENT.open("TradingTrackRecord")

record = SHEET.worksheet("Year 2023")

data = record.get_all_values()

print(data)