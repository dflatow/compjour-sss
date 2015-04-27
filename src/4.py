
import bs4
import requests

response = requests.get('https://www.usajobs.gov/Search?Keyword=librarian&Location=&search=Search&AutoCompleteSelected=False')
soup = bs4.BeautifulSoup(response.text)
d = soup.select('#searchpagerTop > div.resultspager-left > p > span')[2]
print("The number of librarian-related job positions that the federal government is currently hiring for:", d.text.strip(), ".")

