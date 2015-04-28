import json
import requests

data_url = 'https://projects.propublica.org/nonprofits/api/v1/search.json?order=revenue&sort_order=desc'
data = json.loads(requests.get(data_url).text)
result = data['filings'][0]['organization']['name']
print("The non-profit organization with the highest total revenue, according to the latest listing in ProPublica's Nonprofit Explorer:", result)

