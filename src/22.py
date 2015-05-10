
import bs4
import requests

response = requests.get('http://www.senate.gov/general/committee_assignments/assignments.htm')
soup = bs4.BeautifulSoup(response.text)

data = soup.select('table > tr > td > a')
data_list = [x.text for x in data]

ind1 = data_list.index("Boxer, Barbara")
ind2 = data_list.index("Burr, Richard")
print("commities:", ind2 - ind1 - 1)