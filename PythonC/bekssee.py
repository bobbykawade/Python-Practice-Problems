import pandas as pd
data1 = pd.read_csv('Berkeley.csv')
print(data)
total_admit = (data1[data1['Admit'] == 'Admitted']['Freq'].sum())
print(total_admit)
sum_of_admit = data1.groupby('Admit').sum()
total_admit = data1['Freq'].sum()
total_admit = (data1[data1['Admit'] == ])