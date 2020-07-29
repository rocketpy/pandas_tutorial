import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#  for jupyter notebook use:  %matplotlib inline


#  data preparation
df = pd.read_csv('file_name.csv')
# print(df)

# if need remove two data points with notes
new_df = df[df.notes.astype(str) == 'nan'].reset_index(drop=True)

#  print distribution of experience levels
new_df.some_column_name.value_counts()

#  to combine  groups
comb_df = new_df.copy()
comb_df['some_column'] = comb_df.column_name == 'column_name'

#  for make varieties categorical
vars = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
comb_df['favorite'] = pd.Categorical(comb_df['favorite'], categories = varieties)
comb_df['favorites'] = pd.Categorical(comb_df['favorites'], categories = varieties)

