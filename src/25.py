import requests
import bs4
import re

response = requests.get('http://www.safercar.gov/Vehicle+Shoppers/5-Star+Safety+Ratings/2011-Newer+Vehicles/Vehicle-Detail?vehicleId=9096')
soup = bs4.BeautifulSoup(response.text)
data = soup.select("div.star_rating img")
print(data[0].get('title'))