import requests
import bs4
import re

response = requests.get('https://data.ny.gov/browse?sortBy=most_accessed&sortPeriod=month&utf8=%E2%9C%93')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("div.titleLine a.name")
print(data[0].text)