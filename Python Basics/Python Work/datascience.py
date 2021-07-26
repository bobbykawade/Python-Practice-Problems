import pandas as pd
import numpy as np
#to see all coloumns and rows
pd.set_option('display.max_columns',13)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_colwidth', 10)
pd.set_option('display.width', None)
a = pd.read_csv('bank.csv')
print(type (a))
print(a)
# x = pd.DataFrame(data = a)
# keep specific coloumn(series)-
# y = (x[['Geography', 'Age']])
# print(y)

# missing data
#how you drop missing data using dropna()
# a.isnull()
# not_null_data = a.dropna()
# print(not_null_data)
# a.dropna(inplace = True)
# a
# data = [1,2,3,4,5,6,7,np.nan,8,9]
# data1 = pd.Series([1,2,3,4,5,6,7,np.nan,8,9])
# print(data1.isnull())
# missing_surname = pd.isnull(a['Surname1'])
# a = [missing_surname]
# a.isnull()
# not_null_data = a.fillna()
# print(not_null_data)
# a.fillna(inplace = True)
# a
#