import bs4
import requests
import re
import datetime

def parse_dates(data):
	dates = [re.findall('\d+', x.text) for x in data]
	dts = [datetime.date(int(x[0]), int(x[1]), int(x[2])) for x in dates]
	return dts

def count_fridays(dts):

	return len([1 for x in dts if x.weekday() == 4])

response = requests.get('http://www.justice.gov/feeds/opa/justice-news.xml')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("channel pubdate")

print('''In the "Justice News" RSS feed maintained by the Justice Department, the number of items published on a Friday:''', count_fridays(parse_dates(data)))


