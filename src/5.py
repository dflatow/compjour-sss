import pandas as pd

data = pd.read_csv('https://data.consumerfinance.gov/api/views/c8k9-ryca/rows.csv?accessType=DOWNLOAD', 
                   parse_dates = 'Date received',
                   index_col='Date received')

data.sort_index(inplace=True, ascending=False)
print("Most recent consumer complaint involving student loans: ", data.iloc[0].loc['Company'])