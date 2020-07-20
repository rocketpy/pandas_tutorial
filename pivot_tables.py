#  pivot - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot.html
#  pivot_table - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html 
#  DataFrame to ...  - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html

import pandas as pd


# read excel file
df1 = pandas.read_excel("file_name.xlsx", sheetname=0)  # 0 - start from first page
df2 = pandas.read_excel("file_name.xlsx", sheetname=0)

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


# just a simple example
df1 = pd.DataFrame([['a', 'b'], ['c', 'd']],
                   index=['row 1', 'row 2'],
                   columns=['col 1', 'col 2'])

df1.to_excel("result.xlsx")  # ("result.xlsx", sheet_name='Sheet_name_1')    
