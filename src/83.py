# The sum of White House staffermember salaries in 2014
import requests
import csv
url = "https://open.whitehouse.gov/api/views/i9g8-9web/rows.csv?accessType=DOWNLOAD"
txt = requests.get(url).text

# save the file temporarily
f = open("/tmp/salaries2014.csv", "w", encoding="utf-8")
f.write(txt)
f.close()


# reopen
f = open("/tmp/salaries2014.csv", "r", encoding="utf-8")
rows = list(csv.DictReader(f))
totes = 0
for r in rows:
    # remove $ sign, convert to float
    salval = float(r['Salary'].replace('$', ''))
    totes += salval

print(totes)

