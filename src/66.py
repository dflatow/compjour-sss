import pandas as pd
import numpy as np

df = pd.read_csv("../data/min_wages.csv", header=False, names=["state", "min_wage"])
print(df['min_wage'].iloc[np.argmax(df.min_wage)])