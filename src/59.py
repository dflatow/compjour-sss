import bs4
import requests

tag = 'university'

response = requests.get('http://catalog.data.gov/dataset?tags=' + tag)
soup = bs4.BeautifulSoup(response.text)
m = soup.select("div.primary section.module div.new-results")[0]
print("Number of ", tag, " related datasets on data.gov:", m.text.strip())