import pandas as pd
from datetime import datetime


curr_year = datetime.now().year

data = pd.read_csv('https://www.osha.gov/dep/fatcat/fy15_federal-state_summaries.csv', parse_dates = ['Date of Incident'], index_col = ['Date of Incident'])
result = sum((data.index.year == curr_year) & (data['Fatality or Catastrophe'] == 'Fatality'))
print("The number of workplace fatalities at reported to the federal and state OSHA in the latest fiscal year:", result)