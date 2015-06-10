
import requests
import json
import re

data_url = "https://analytics.usa.gov/data/live/top-pages-realtime.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

print(re.findall("[a-zA-Z0-9]+\.gov", data['data'][0]['page'])[0])

