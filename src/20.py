import pandas as pd

data = pd.read_csv('../data/osha_inspection.csv')
print(data.head())

print("The number of OSHA enforcement inspections involving Wal-Mart in California since 2014:")