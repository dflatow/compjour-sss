import bs4
import requests

response = requests.get('https://www.clinicaltrials.gov/')
soup = bs4.BeautifulSoup(response.text)
d = soup.select('body div[id="wrapper"] p span.highlight')[0]
print("Total number of clinical trials as recorded by the National Institutes of Health is", d.text, ".")