import pandas as pd
df = pd.read_csv("../data/mega_millions.csv")
numbers = ' '.join(df['Winning Numbers'].values).split(" ")
numbers = [int(x) for x in numbers]
s = pd.Series(numbers)
print(s.value_counts().index[0])