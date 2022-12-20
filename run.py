# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import gspread
from datetime import datetime
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

"""
record = SHEET.worksheet("Year 2023")

data = record.get_all_values()

print(data)
"""
def get_date():
    """
    The user has to enter the exact date.
    If the value is incorrect, a message will be
    displayed and the user will have to re-enter the correct date.
    """
    print("Hello, enter the date of your trading session.")
    print("The date must follow the following structure:")
    print("Two-digit day, two-digit month, Four-digit year  (example: 11-03-2023).")

    while True:
        try:
            day_session = input("Enter date:")
            datetime.strptime(day_session,'%d-%m-%Y')
            print(f"{day_session} in valid :)")
            break
        except ValueError:
            print("The date entered is incorrect")

get_date()