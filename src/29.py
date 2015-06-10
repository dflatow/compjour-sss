import requests
from lxml import html
response = requests.get('https://www.tdcj.state.tx.us/death_row/dr_scheduled_executions.html')
doc = html.fromstring(response.text)
print(doc.cssselect('td')[0])
