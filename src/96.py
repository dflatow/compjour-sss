import requests
import bs4
import re

response = requests.get('http://www.supremecourt.gov/oral_arguments/calendars/MonthlyArgumentCalApril2015')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("table.MsoTableGrid")[0].select("> tr")
print(len(data))