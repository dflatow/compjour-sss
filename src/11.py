import pandas as pd

data = pd.read_csv('http://www2.census.gov/govs/statetax/14staxcd.txt', index_col=[0])
print("California collected ", 1.0 * data.loc['T01'].loc['CA'] / 1e6 ," billion dollars in property taxes, according to the U.S. Census 2013 Annual Survey of State Government Tax Collections")