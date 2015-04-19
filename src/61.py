import bs4
import requests


response = requests.get('http://www.state.gov/secretary/travel/index.htm')
soup = bs4.BeautifulSoup(response.text)
m = soup.select("body div#dos-wrapper div#content-output div.travel-wrap li#total-mileage span")[0]
print("The number of miles traveled by the current U.S. Secretary of State: ", m.text.strip())