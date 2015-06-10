import pandas as pd
df = pd.read_csv("../data/tsa_guns.csv", skiprows=2, header=True)
print(sum(df['CHAMBERED?'] == "Y"))