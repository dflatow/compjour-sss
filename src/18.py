import pandas as pd

data = pd.read_csv('http://unitedstates.sunlightfoundation.com/legislators/legislators.csv')
print("The number of U.S. congressmembers who have Twitter accounts, according to Sunlight Foundation data:",
	   data.count().loc['twitter_id'])