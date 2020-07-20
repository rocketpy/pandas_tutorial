#  pivot - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot.html
#  pivot_table - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.pivot_table.html 
#  DataFrame to ...  - https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_excel.html

import pandas as pd


# read excel file
df1 = pandas.read_excel("file_name.xlsx", sheetname=0)  # 0 - start from first page
df2 = pandas.read_excel("file_name.xlsx", sheetname=0)

# create a spreadsheet-style pivot table as a DataFrame

