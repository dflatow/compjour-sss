
import bs4
import requests


response = requests.get('https://instagram.com/tsa/')
soup = bs4.BeautifulSoup(response.text)

m = soup.select("#react-root span.sCount")
print(m)

