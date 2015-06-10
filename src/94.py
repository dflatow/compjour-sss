import pandas as pd
df = pd.read_csv("../data/SAT_results.csv")
df = df[df["SAT Math Avg. Score"] != "s"]
df["SAT Math Avg. Score"] = df["SAT Math Avg. Score"].astype(int)
print(df.sort("SAT Math Avg. Score", ascending=False).iloc[0]['SCHOOL NAME'])