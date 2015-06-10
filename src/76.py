import requests
import bs4
import re

response = requests.get('http://www.gao.gov/browse/topic')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("span")
print(data[0].text.strip("()"))