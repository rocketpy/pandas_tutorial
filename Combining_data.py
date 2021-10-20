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

# result = temp[temp["Number"] == "12345"]
# result.head()

# inner_merged = pd.merge(result, temp_data)
# inner_merged.head()

inner_merged_data = pd.merge(temp_data, result, on=["PLACE", "DATE"])
# inner_merged_data.head()
# inner_merged_data.shape


# Outer Join
outer_merged = pd.merge(temp_data, result, how="outer", on=["PLACE", "DATE"])
# outer_merged.head()
# outer_merged.shape

# Left Join
left_merged = pd.merge(temp_data, result, how="left", on=["PLACE", "DATE"])
# left_merged.head()
# left_merged.shape






