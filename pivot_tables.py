#  pivot - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot.html
#  pivot_table - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html 
#  DataFrame to ...  - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html
"""
For anyone who is still interested in the difference between pivot and pivot_table, there are mainly two differences:
- pivot_table is a generalization of pivot that can handle duplicate values for one pivoted index/column pair.
  Specifically, you can give pivot_table a list of aggregation
  functions using keyword argument aggfunc. The default aggfunc of pivot_table is numpy.mean.
- pivot_table also supports using multiple columns for the index and column of the pivoted table. A hierarchical index will be automatically generated for you.

- pivot_table will only allow numerical types as "values=", whereas pivot will take string types as "values=".
- pivot() doesn't accept a list for index.
  pivot_table() accepts.
  Internally, both of them are using reset_index()/stack()/unstack() to do the job.
"""

import pandas as pd


# read excel file
df1 = pd.read_excel("file_name.xlsx", sheetname=0)  # 0 - start from first page
df2 = pd.read_excel("file_name.xlsx", sheetname=0)

# very important !!! before print data use this :
print(df1.head(10))  # first 10 rows
print(df2.head(10))  # first 10 rows

# from df1 and df2 take some columns
date = df1['column_name']
variable = df1['column_name']
value = df2['column_name']
result = df.pivot(index='date', columns='variable', values='value')
result.to_excel("result.xlsx")


#  aggfunc='mean' is the default 
df.pivot_table(values='column_name', index='row', columns='col', fill_value=0, aggfunc='mean')  # aggfunc='sum'

#  pd.DataFrame.groupby
df.groupby(['row', 'col'])['col_name'].mean().unstack(fill_value=0)

# pd.crosstab
pd.crosstab(index=df['row'], columns=df['col'], values=df['col_name'], aggfunc='mean').fillna(0)

# get something other than mean, like sum
df.pivot_table(values='col_name', index='row', columns='col', fill_value=0, aggfunc='sum')  #  aggfunc='mean'

# pd.DataFrame.groupby
df.groupby(['row', 'col'])['col_name'].sum().unstack(fill_value=0)

#  convert rows as column headers
pivot_table = df.pivot_table('numb of ...', ['Year', 'Country'], 'type')  

#  to reorder the columns
typy_of_color.reindex_axis(['Gold', 'Silver', 'Bronze'], axis=1)

#  Stack/ Unstack will bring the lowest level of column index to the lowest level of row index
df.set_index(['year', 'country', 'type_of_color'], drop=True).unstack('type_of_color')


#  return reshaped DataFrame organized by given index / column values
df = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two',
                           'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})

pivot_table = df.pivot(index='foo', columns='bar', values='baz')
# or
pivot_table = df.pivot(index='foo', columns='bar', values=['baz', 'zoo'])

pivot_table.to_excel("result.xlsx")


# create a spreadsheet-style pivot table as a DataFrame
df = pd.DataFrame({"A": ["foo", "foo", "foo", "foo", "foo",
                         "bar", "bar", "bar", "bar"],
                   "B": ["one", "one", "one", "two", "two",
                         "one", "one", "two", "two"],
                   "C": ["small", "large", "large", "small",
                         "small", "large", "small", "small",
                         "large"],
                   "D": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "E": [2, 4, 5, 5, 6, 6, 8, 9, 9]})

pivot_table = pd.pivot_table(df, values='D', index=['A', 'B'],
                    columns=['C'], aggfunc=np.sum)

pivot_table.to_excel("result.xlsx")


#  concatenate pandas objects along a particular axis with optional set logic along the other axes
pd.concat([df1, df2])
# or
bigdata = pd.concat([data1, data2], ignore_index=True, sort=False)


# just a simple example
df = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])

df.to_excel("result.xlsx")  # ("result.xlsx", sheet_name='Sheet_name_1')    
