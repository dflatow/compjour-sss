import requests
from lxml import html
# response = requests.get('http://quickfacts.census.gov/qfd/states/26/2622000.html')
doc = html.fromstring(open('../data/detroit.html').read()) 
print(open('../data/detroit.html').read())
td = doc.cssselect('table tbody')[0]
print(td.get("headers"))
print("done")