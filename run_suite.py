import os
import datetime

browser = input('On which browser do you want to run test cases? ')
report = input('Generate HTML report: ')


now = datetime.datetime.now()
if report.lower() == 'yes' or report.lower() == "y" or report.lower() == "":
    report = f'--html=./Reports/report_{now.strftime("%H%M%S")}.html'
else:
    report = ""

if browser == "":
    browser = 'chrome'

command = f"pytest -v {report} ./TestCases/ --browser {browser}"
print(command)
os.system(command)