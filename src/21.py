import bs4
import requests

response = requests.get('http://forecast.weather.gov/MapClick.php?CityName=Gatlinburg&state=TN&site=MRX&textField1=35.7234&textField2=-83.4937&e=0#.VSyOJBPF9dE')
soup = bs4.BeautifulSoup(response.text)
humidity = soup.select('table[id="current_conditions_detail"] tr td')[1]
print("The current humidity level at Great Smoky Mountains National Park is", humidity.text, ".")