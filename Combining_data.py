# Combining data with merge(), .join(), concat()

import pandas as pd


temp_data = pd.read_csv("temp.csv")
time_data = pd.read_csv("time.csv")

print(temp_data.head())
print(time_data.head())

# in Jupyter Notebook
# temp_data.head()
# time_data.head()

# temp_data.shape
# time_data.shape
