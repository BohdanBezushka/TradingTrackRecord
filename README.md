# **TradingTrackRecord** 📈📉

[*Live link to website.*](https://trading-track-record.herokuapp.com/)
![image5](https://user-images.githubusercontent.com/94321555/209341093-223ddd63-470d-4a32-862f-ff021357ba91.png)

This is TradingTrackRecord's Python terminal and is deployed on Heroku using Code Institute's mock terminal template.

The project is designed for people involved in trading. It allows the user to record their trade, write down any important details and see a complete summary of all trading days.

## Contents
* [User Experience - UX](#User-Experience---UX)
  * [User Stories](#User-Stories)
* [Flowchart](#Flowchart)
* [Colour Scheme](#Colour-Scheme)
* [Database structure](###Database-structure)
* [Features](#Features)
  * [Menu](#Menu)
  * [Option 1](#Option-1)
  * [Option 2](#Option-2)
  * [Features Left to Implement](#Features-Left-to-Implement)
* [Technologies Used](#Technologies-Used)
  * [Languages](#Languages)
  * [Software](#Software)
  * [Imported Libraries and Packages](#Imported-Libraries-and-Packages)
* [Testing and Validation](#Testing-and-Validation)
* [Bugs](#Bugs) 
* [Unfixed Bugs](#Unfixed-Bugs)
* [Deployment](#Deployment)
  * [Local Deployment](#Local-Deployment)
  * [Heroku Deployment](#Heroku Deployment)
* [Credits](#Credits)
  * [Information Resources](#Information-Resources)
  * [Content](#Content)
  * [Acknowledgements](#Acknowledgements)

## User experience - UX
### User Stories
- As a user, I want to be able to clearly see the name of the site at the top of the page.
- As a user, I want to be able to enter the date of the operation.
- As a user, I want to be able to enter the result of the trade.
- As a user, I want to be able to indicate whether I have followed my own trading rules.
- As a user, I want to be able to note any important details of the trade.
- As a user, I want to be able to see a complete summary of the trades.


## Flowchart
I made this flowchart before writing my code to have a clear view of what needed to be implemented while writing the program. It clearly 
indicates the layout and structure of the program, 
including where the user has to be prompted for input, 
where the computer much check the input and how to handle 
invalid input. It has been created in [*Lucid Chart*](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=_chart_en_tier1_mixed_search_brand_exact_&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=aud-809923745462:kwd-55720648523&km_CPC_Country=1007850&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=CjwKCAiAnZCdBhBmEiwA8nDQxXWBs0Kl2WhtETFgmgeecLRbAHVP82ljQ65_j11XE3EIcXX8v7s9whoCW3QQAvD_BwE).

## Colour Scheme
As this program was built for the terminal, there wasn't much in terms of design or colour but I did use [*Colorama*](https://pypi.org/project/colorama/) to add a bit of colour where I felt was needed within the terminal to make certain parts stand out to the user.
![image21](https://user-images.githubusercontent.com/94321555/209341275-b64b06a6-8032-4ef5-abec-3fc685c31ab7.png)

## Database structure
The Google Sheets service is used to store the project database in the spreadsheet. There is a spreadsheet to record the trades:

![image11](https://user-images.githubusercontent.com/94321555/209341380-2161750b-5a41-40c6-85f9-5ac315d4372f.png)
The main table consists of four columns: Date, Amount, Implementation and Notes.

## Features
### Menu
We welcome the user and give him the option to register his trade or the option to view a full summary of trades.
![image16](https://user-images.githubusercontent.com/94321555/209341517-a479b0cb-b9db-4a92-a024-f8e7af587396.png)

### Option 1
The user initiates the registration of his trade. First of all he has to indicate a date. There is a description of how to do this and an example. Here I use [*DateTime*](https://pypi.org/project/DateTime/) to check the date.
![image19](https://user-images.githubusercontent.com/94321555/209341628-7ad1a22e-44b0-49f7-bfcd-ca09ce1dd97a.png)

In case of an incorrect date,  a message is displayed to the user and a correct date is requested again.
![image14](https://user-images.githubusercontent.com/94321555/209341723-ef1174ca-2628-4cea-b4a6-21b4c1af64cf.png)

If the date is correct, I confirm it to the user and ask him to enter the result of his trade. For this, I show several examples of how to enter the correct amount.
![image1](https://user-images.githubusercontent.com/94321555/209341801-5f605f76-f01d-475c-a316-064a6e78dd34.png)

In case the amount is incorrect, a message is displayed to the user and a correct amount is requested again.
![image13](https://user-images.githubusercontent.com/94321555/209341879-b17c637d-3bf1-405a-a332-99611d8a126c.png)

If the amount is correct, I confirm it to the user. Then the user must write YES if he has followed his trading plan or NO if he hasn't.
![image10](https://user-images.githubusercontent.com/94321555/209341977-e67bb9ce-a01e-4b38-9c9d-9373ef6d0183.png)

In case the answer is not valid, a message is displayed to the user and a correct answer is requested again.
![image6](https://user-images.githubusercontent.com/94321555/209342075-6629a82d-0abd-45ad-ace7-5bbcbe78c64d.png)

If the answer is YES, I show a happy face and then I ask him to detail his trading.
![image4](https://user-images.githubusercontent.com/94321555/209342155-21bcbe63-f7be-4b72-acbe-dec00eedce7e.png)

If the answer is NO, I show a sad face and then I ask him to write down why he has failed in his trading plan and to give some relevant details.
![image2](https://user-images.githubusercontent.com/94321555/209342197-f9cbe6a0-b961-49d8-8552-f5995828365e.png)

After the description, the worksheet is updated and returns to the menu automatically.
![image20](https://user-images.githubusercontent.com/94321555/209342273-040e6290-8f70-4143-a740-714c8cb352ce.png)

If the user enters option 2, a complete record of all trades is displayed. It also gives the option to return to the menu when the user types YES.
![image7](https://user-images.githubusercontent.com/94321555/209342354-18dc04e4-164c-4b12-921b-98f288e23a28.png)

### Features Left to Implement
- Create a third option: display the cumulative amount of the sum of all trades.

- Create a fourth option: view a graph of the evolution of the capital.

## Technologies Used
### Languages
- [*Python*](https://www.python.org/) - high-level, general-purpose programming language.
- [*Markdown*](https://en.wikipedia.org/wiki/Markdown) - markup language used to write README and TESTING documents.

### Software
- [*Google Sheets*](https://www.google.com/sheets/about/) is used to store the leaderboard.
- [*Google Cloud*](https://devlibrary.withgoogle.com/products/cloud?sort=updated) was used to enable the APIs needed for this project.
- [*Github*](https://github.com) was used to store the project's code after being pushed from Git.
- [*Gitpod*](https://www.gitpod.io/) terminal was used to commit my code using Git and push it to Github.
- [*Git*](https://git-scm.com/) was used for version control through the Gitpod terminal.
- [*Ui.dev*](https://ui.dev/amiresponsive?url=https://trading-track-record.herokuapp.com/) was used to generate mockups for the project.
- [*Heroku*](https://www.heroku.com), online app used to deploy project.
- [*LucidChart*](https://www.lucidchart.com) was used to create flow diagram.
- [*PEP8 Python Validator*](https://pep8ci.herokuapp.com/) to see errors in the code.

### Imported Libraries and Packages
- [*Gspread*](https://docs.gspread.org/en/v5.7.0/) was used to link the program to Google Sheets to read and update the leaderboard.
- [*Colorama*](https://pypi.org/project/colorama/) was used to add colour to some aspects of the program to make certain parts stand out.
- [*DateTime*](https://pypi.org/project/DateTime/) was used to obtain a valid date from the user.
- [*PrettyTable*](https://pypi.org/project/prettytable/) - python library for easily displaying tabular data in a visually appealing ASCII table format.

## Testing and Validation
View Testing and Validation [*here*](TESTING.md).

## Bugs
**First:** I want the date entered by the user to be updated in the spreadsheet. The terminal shows me the following:
![image3](https://user-images.githubusercontent.com/94321555/209342449-f637883f-dc6b-4164-abc5-80735c76f7a0.png)

The solution is to put the date in brackets. I show you the code below:
![image12](https://user-images.githubusercontent.com/94321555/209342512-a02ffab2-e8aa-412f-84d0-8e3eba48b470.png)
But I don't understand why in the section "Love Sandwiches Walkthrough Project > Adding Sales Data > Updating our sales worksheet" the function enters the data into the worksheet without brackets. 🤔

**Second:** When I installed the project on Heroku the terminal does not show up and displays the following error:

File "/app/run.py", line 14, in <module>
    TRADINGTRACKRECORD = Credentials.from_service_account_file("tradingtrackrecord.json")
  File "/app/.heroku/python/lib/python3.10/site-packages/google/oauth2/service_account.py", line 241, in from_service_account_file
    info, signer = _service_account_info.from_filename(
  File "/app/.heroku/python/lib/python3.10/site-packages/google/auth/_service_account_info.py", line 79, in from_filename
    with io.open(filename, "r", encoding="utf-8") as json_file:
FileNotFoundError: [Errno 2] No such file or directory: 'tradingtrackrecord.json'

To fix this I rewrote the following lines of code. This is before:
![image22](https://user-images.githubusercontent.com/94321555/209342642-7cbfd279-f14d-489d-acdb-a30fa753aeac.png)

After:
![image15](https://user-images.githubusercontent.com/94321555/209342805-95b28df9-8e16-490b-a8bf-7db96bc27b92.png)

**Third:** Syntax errors in PEP8 Python Validator:
![image8](https://user-images.githubusercontent.com/94321555/209342917-5c6bb0ab-aed3-4630-a5b7-86a2e14cad53.png)

![image9](https://user-images.githubusercontent.com/94321555/209342970-ccd9ea93-7ab5-44c3-9b4a-dceaad9133d3.png)

![image17](https://user-images.githubusercontent.com/94321555/209343017-ff3e82a7-1f98-4b09-8b6d-3a7e858ec4cf.png)

The solution is to look at every line of code that has an error and fix it.
![image18](https://user-images.githubusercontent.com/94321555/209343076-23b3976d-347c-4496-b9ff-b93d73dca51a.png)

## Unfixed Bugs
No unfixed bugs.

## Deployment
Code Institute has provided a [template](https://github.com/Code-Institute-Org/python-essentials-template) to display the terminal view of this backend application in a modern web browser. This is to improve the accessibility of the project to others.

The live deployed application can be found at [*TradingTrackRecord*](https://trading-track-record.herokuapp.com/)

### Local Deployment
To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/BohdanBezushka/TradingTrackRecord.git`

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Further down, to support dependencies, select *Add Buildpack*.
- The order of the buildpacks is important, select `Python` first, then `Node.js` second. (if they are not in this order, you can drag them to rearrange them)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

## Credits

### Information Resources
- [*CBEA*](https://cbea.ms/git-commit/) and [*FreeCodeCamp*](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/) to improve the writing of commits.

- [*Github*](https://github.com/burnash/gspread/issues/828) to solve the first bug.

- The documentation of [*gspread*](https://docs.gspread.org/en/v5.7.0/), [*colorama*](https://pypi.org/project/colorama/), [*datetime*](https://pypi.org/project/DateTime/) and [*prettytable*](https://pypi.org/project/prettytable/).

## Content
I came up with the idea because I am in the trading business and in the future I would like to create a quality software for investors.

### Acknowledgements
Special thanks to my mentor [*Mitko Bachvarov*](https://www.linkedin.com/in/mitko-bachvarov-40b50776/) and my colleagues at [*Code Institute*](https://codeinstitute.net/ie/).
