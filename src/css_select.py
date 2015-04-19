import bs4
import requests


response = requests.get('http://developerexcuses.com/')
soup = bs4.BeautifulSoup(response.text)
m = soup.select("body > div.wrapper > center > a")[0]
print(m.text)

