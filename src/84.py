import requests
import bs4
import re

response = requests.get('https://www.federalregister.gov/articles/search?conditions%5Bpublication_date%5D%5Bis%5D=06%2F10%2F2015&conditions%5Btype%5D=NOTICE')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("div.article_count h2.title_bar")[0]
print(data.text)


