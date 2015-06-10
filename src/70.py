import pandas as pd
df = pd.read_csv("../data/whitehouse_salaries.csv")
df['Salary'] = df['Salary'].apply(lambda x: float(x.strip("$,")))
print(df[df['Status'] == "Employee"]['Salary'].max())