
import requests
import json
import re

data_url = "https://analytics.usa.gov/data/live/realtime.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

print(data['data'][0]['active_visitors'])
