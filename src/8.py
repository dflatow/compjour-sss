import pandas as pd

data = pd.read_csv('https://health.data.ny.gov/api/views/dk4z-k3xb/rows.csv?accessType=DOWNLOAD')
result = data['Comparison Results'].value_counts().loc['Rate significantly higher than Statewide Rate']
print('''The number of times when a New York heart surgeon's rate of patient deaths \
for all cardiac surgical procedures was "significantly higher" than the statewide \
rate, according to New York state's analysis:''', result)