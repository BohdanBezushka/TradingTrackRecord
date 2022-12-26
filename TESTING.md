## __Code Validation__
I validated run.py file using [Code Institute's Python Linter](https://pep8ci.herokuapp.com/) and was met with no errors.

| File Validated | Image |
| -------------- | ----- |
| [run.py](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/BohdanBezushka/TradingTrackRecord/main/run.py) | (https://github.com/adamgilroy22/python-hangman/blob/main/documentation/testing/user-story-1-a.png)

## __User Stories Testing__
| User Goal | Requirement met | Image(s) |
| --------- | --------------- | -------- |
| As a user, I want to be able to clearly see the name of the site at the top of the page.| Yes |![image16](https://user-images.githubusercontent.com/94321555/209486067-20c1432f-dfaa-4097-a73e-3554f77c3738.png) |
| As a user, I want to be able to enter the date of the operation. | Yes | ![image19](https://user-images.githubusercontent.com/94321555/209486094-238c57c2-0ac5-4c53-82a3-1d5087ce1ecc.png) |
| As a user, I want to be able to enter the result of the trade. | Yes | ![image1](https://user-images.githubusercontent.com/94321555/209486130-ab17f3e8-4cb5-4ab7-8ddc-2f81ffc36e8d.png) |
| As a user, I want to be able to indicate whether I have followed my own trading rules. | Yes | ![image10](https://user-images.githubusercontent.com/94321555/209486142-a620c315-acbf-4936-918b-6534e6dca048.png) |
| As a user, I want to be able to note any important details of the trade. | Yes | ![image2](https://user-images.githubusercontent.com/94321555/209486184-8dad7bb5-c7e0-40db-829b-54acd26d55cf.png) |
| As a user, I want to be able to see a complete summary of the trades.| Yes | ![image7](https://user-images.githubusercontent.com/94321555/209486201-f867f10c-07b0-46d3-beef-fbaaec48eae2.png)|


## __Program Validation Testing__
| Section Tested | Input To Validate | Expected Outcome | Actual Outcome | Pass/Fail |
| -------------- | ----------------- | ---------------- | -------------- | --------- |
| Start Program | N/A | Load welcome message and prompt user to enter option 1 or option 2 | As expected | PASS |
| Enter Menu Option | Input Menu | Notify user that this isn't a valid input and loop back  | As expected | PASS |
| Enter Menu Option | Input "1" |Require the user to indicate the date of the trade | As expected | PASS |
| Enter Menu Option | Input "2" | Show the user a summary of the entries | As expected | PASS |
| Enter Date | Input incorrect date | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Date | Input correct date| Notify the user to write the result of the trade| As expected | PASS |
| Enter Amount | Input incorrect amount |Notify user that this isn't a valid input and loop back | As expected | PASS |
| Enter Amount | Input correct amount | Ask the user if he has followed his trading plan.| As expected | PASS |
| Trading plan | Input incorrect answer | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Trading plan | Input "YES" | Ask to note details of the trade | As expected | PASS |
| Trading plan | Input "NO" | Ask to note details of the trade | As expected | PASS |
| Enter notes | Input | Confirm that the data has been updated correctly and return to the menu. | As expected | PASS |
| Summary | Input incorrect answer | Notify user that this isn't a valid input and loop back | As expected | PASS |
| Summary | Input "YES" | Return to the start menu. | As expected | PASS |

## __Cross-browser Testing__
After deploying the program through Heroku, I have tested it on Chrome, Firefox and Edge. The program has loaded perfectly and had no issues running as expected across all browsers.

| Browser | Image |
| ------- | ----- |
| Chrome | ![Captura de pantalla (520)](https://user-images.githubusercontent.com/94321555/209486258-cb1be1cd-90d4-4d40-9655-d11e7b29dc66.png) |
| Firefox | ![Captura de pantalla (518)](https://user-images.githubusercontent.com/94321555/209486273-33197728-98ec-4360-bc8b-be3216e3541e.png) |
| Edge | ![Captura de pantalla (519)](https://user-images.githubusercontent.com/94321555/209486288-d653c350-ad8f-4071-bbd9-ae4b60d8708d.png) |
