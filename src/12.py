import pandas as pd

data = pd.read_excel('http://www.faa.gov/airports/planning_capacity/passenger_allcargo_stats/passenger/media/cy10_primary_enplanements.xls')
print("In 2010, the year-over-year change in enplanements at America's busiest airport is {0:0.2}%".format(data["% Change"].iloc[0] * 100.0))