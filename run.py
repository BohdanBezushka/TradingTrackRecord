import gspread
from datetime import datetime
from google.oauth2.service_account import Credentials
from prettytable import PrettyTable
import colorama
from colorama import Fore, Style

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

TRADINGTRACKRECORD = Credentials.from_service_account_file("tradingtrackrecord.json")
SCOPED_TRADINGTRACKRECORD = TRADINGTRACKRECORD.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_TRADINGTRACKRECORD)
SHEET = GSPREAD_CLIENT.open("TradingTrackRecord")

# 1.Register trade.
def get_date():
    """
    The user has to enter the exact date.
    If the value is incorrect, a message will be
    displayed and the user will have to re-enter the correct date.
    """
    print("\033[32mHello, enter the date of your trading session.\033[0m\n")
    print("\033[32mThe date must follow the following structure:\033[0m\n")
    print("\033[32mTwo-digit day, two-digit month, Four-digit year (example: 11-03-2023).\033[0m\n")

    while True:
        """
        The user has to enter an exact date if not the loop 
        will repeatedly request data, until it is valid.
        """
        try:
            day_session = input("\033[33mEnter date:\033[0m\n")
            datetime.strptime(day_session,'%d-%m-%Y')
            print(f"{day_session} is valid :)")
            break
        except ValueError:
            print("\033[31mThe date entered is incorrect!\033[0m\n")
    return day_session

def get_amount():
    """ 
    The user has to enter the profit or loss.
    If the value is incorrect, a message will be
    displayed and the user will have to re-enter the correct date.
    """
    print("\033[32mPlease enter the result of the investment operation below.\033[0m\n")
    print("\033[32mThe quantity can be negative, positive or zero.\033[0m\n")
    print("\033[32mThere can be a maximum of two decimal places.\033[0m\n")
    print("\033[32mExample: -100.32, 0.00, 220.80\033[0m\n")

    while True:
        """
        The user has to enter an exact amount if not the loop will repeatedly request data, until it is valid.
        """
        try:
            money = float(input("\033[33mEnter amount:\033[0m\n"))
            print(f"{format(money, '.2f')} is valid.")
            break
        except ValueError:
            print("\033[31mYou entered an incorrect value!\033[0m\n")
    return money

def get_implementation():
    """ 
    The user has to indicate YES or NO. 
    """
    print("\033[32mHave you followed your trading plan?dfsf\033[0m\n")
    print("\033[32mIndicate only with a YES or NO.\033[0m\n")

    while True:
        """
        If no YES or NO is received, an error message will
        be displayed to the user and the loop will continue to run.
        """
        answer = input("\033[33mHave you followed your trading plan? (YES/NO):\033[0m\n")
        if answer.upper() == "YES":
            print("\033[32mYou respected your investment rules ;)\033[0m\n")
            break
        elif answer.upper() == "NO":
            print("\033[32mYou didn't respect your investment rules :(\033[0m\n")
            break
        else:
            print("\033[31mYou didn't give a correct answer!\033[0m\n")
    return answer

def get_notes():
    """
    The user has to describe the most relevant details of the daily operation.
    """
    print("\033[32mDescribe your operation clearly and precisely.\033[0m\n")
    print("\033[32mIf you have not complied with your trading plan, please indicate the reason.\033[0m\n")
    note = input("\033[33mDescribe your trade:\033[0m\n")
    return note

def update_date_worksheet(date,data_money,implementation,description):
    """
    Update the worksheet, add the date and amount specified by the user in the "Date" column. 
    """
    print("\033[32mAdding data to the TradingTrackRecord worksheet.\033[0m\n")
    date_worksheet = SHEET.worksheet("2023")
    date_worksheet.append_row([date,data_money,implementation,description])
    print("\033[32mData updated successfully.\033[0m\n")


def main_program():
    """
    Run all program functions.
    """
    date = get_date()
    data_money = get_amount()
    implementation = get_implementation()
    description = get_notes()
    update_date_worksheet(date,data_money,implementation,description)


# 2.Show track record.

def print_all_data():
    """
    Gets all values from the spreadsheet and prints them 
    on the terminal in the form of a table 
    generated with the PrettyTable library.
    """
    table = PrettyTable()
    table.field_names = ["Date", "Amount", "Implementation", "Notes"]
    table._max_table_width = 180
    all_data = SHEET.worksheet("2023").get_all_values()
    all_data_no_headers = all_data[1:]

    
    for i in all_data_no_headers:
        # Each iteration adds a row to the table, skips the headers.
        table.add_rows(
            [i[:]]
        )
    print(table)

#Programme start:

def start_menu():
    """ 
    This is what the user sees at the start of the programme.
    The user will have option 1 to record his daily operation 
    and option 2 to see a summary of the entire worksheet.
    """
    print("\n" * 2)
    print(" " * 20 + "\033[3;1;4;33mWelcome to TradingTrackRecord\033[0m")
    print(" " * 13 + '"The recording of daily trades is fundamental')
    print(" " * 17 + 'to improve as an investor and that')
    print(" " * 22 + 'is why you are here."')
    print("\n" * 2)

    print("\033[32mIf you want to register your trade type: 1.\033[0m\n")
    print("\033[32mIf you want to see the full summary type: 2.\033[0m\n")
    
    while True:
        option = input("\033[33mWhat do you want to do? (1/2):\033[0m\n")
        if option == "1":
            print("\033[32mStarting trade registration...\033[0m\n")
            main_program()
            start_menu()
            break
        elif option == "2":
            print("\033[32mStarting summary display...\033[0m\n")
            print_all_data()
            break
        else:
            print("\033[31mYou didn't give a correct answer.\033[0m\n")

start_menu()