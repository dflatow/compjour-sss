import pandas as pd

data = pd.read_csv("http://www.asias.faa.gov/pls/apex/f?p=100:93::FLOW_EXCEL_OUTPUT_R2161113456916636_en")
print("The total number of preliminary reports on aircraft safety incidents/accidents in the last 10 business days:", len(data))