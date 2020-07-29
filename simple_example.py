import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#  for jupyter notebook use:  %matplotlib inline


#  data preparation
df = pd.read_csv('file_name.csv')
# print(df)

# if need remove two data points with notes
new_df = df[df.notes.astype(str) == 'nan'].reset_index(drop=True)
