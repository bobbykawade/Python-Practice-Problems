import pandas as pd
import numpy as np
#to see all coloumns and rows
pd.set_option('display.max_columns',13)
pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_colwidth', 10)
pd.set_option('display.width', None)
a = pd.read_csv('contacts1.csv')
print(type (a))
print(a)