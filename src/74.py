import requests
import bs4
import re

response = requests.get('http://gov.georgia.gov/bills-signed/2015')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("tr td a")
print(data[0].text)



