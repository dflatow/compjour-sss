import pandas as pd 

data = pd.read_csv("../data/wildlife.csv")
print("Total number of wildlife strike incidents reported at San Francisco International Airport:", len(data))