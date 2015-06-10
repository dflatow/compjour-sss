import requests
import bs4
import re

response = requests.get('https://supreme.justia.com/cases/federal/us/576/13-628/')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("div#opinion li")
print(re.findall("\(.*\)", data[1].text)[0])