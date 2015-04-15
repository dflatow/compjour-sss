import bs4
import requests

response = requests.get('http://www.gao.gov/browse/topic')
soup = bs4.BeautifulSoup(response.text)
d = soup.select('ul.column a[href="/browse/topic/Veterans"]')[0].next_sibling.next_sibling.next_element
print("The number of Government Accountability Office reports and testimonies on the topic of veterans:", d.strip('() '), ".")