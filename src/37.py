import bs4
import requests

response = requests.get('https://www.cia.gov/about-cia/leadership')
soup = bs4.BeautifulSoup(response.text)
d = soup.select('div#content-core div div')[1]
print("The last time the CIA's Leadership page has been updated:", d.text.strip(), ".")