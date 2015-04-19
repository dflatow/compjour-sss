import requests
import json


data_url = "https://analytics.usa.gov/data/live/ie.json"
# fetch the data file
response = requests.get(data_url)
text = response.text
# parse the data
data = json.loads(text)

print("The number of people who visited a U.S. government website using Internet Explorer 6.0 in the last 90 days:", data['totals']['ie_version']['6.0'])