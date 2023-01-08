import os

browser = input('On which browser do you want to run test cases? ')
report = input('Generate HTML report: ')

if report.lower() == 'yes':
    report = '--html=./Reports/report.html'

else:
    report = ""

command = f"pytest -v -s {report} ./TestCases/ --browser {browser} --debug_mode"
print(command)
os.system(command)