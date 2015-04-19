import bs4
import requests


response = requests.get('https://analytics.usa.gov/')
soup = bs4.BeautifulSoup(response.text)

total_visits = soup.select("html body div.container div#main_data section.section_subheadline span")[0].text#.strip()
print(total_visits)
#fraction_ie = soup.select("")[0].text.strip()



#print("The number of people who visited a U.S. government website using Internet Explorer 6.0 in the last 90 days: ", m.text.strip())