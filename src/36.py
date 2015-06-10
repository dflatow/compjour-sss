import csv
import requests
from io import StringIO
CSVURL = '../data/WhiteHouse-WAVES-2012.csv'
data = csv.DictReader(open(CSVURL, encoding='utf-8'))
rows = list(data)
print(len(rows))