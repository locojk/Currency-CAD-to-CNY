# Currency-CAD-to-CNY
This script is a simple program that retrieves the exchange rate for Chinese Yuan (CNY) to Canadian Dollar (CAD) from the Bank of Canada's API.

Requirements
The script requires Python 3 and the requests library. You can install the requests library using pip by running pip install requests in your command line.

Usage
Download the script.
Run the script using python by python main.py
The script will output the newest exchange rate for CNY to CAD, and whether it has increased or decreased since the previous rate.

API
The script uses the following API: https://www.bankofcanada.ca/valet/observations/FXCADCNY/json

Output
The output will be in the following format:

The newest rate change for CNY to CAD is x.xx, 1 Canada Dollar equal to x.xx Chinese Yuan
The rate has increased/decreased by x.xx from the previous observation.
