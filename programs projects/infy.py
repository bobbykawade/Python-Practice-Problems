import math
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
#from nsepy import get_history
#from dateline import date
#from nsetools import NSE
#label attributes
#features- open high low
import pandas as pd
#data = pd.read_csv('dta.csv')
#print(data)
#nse = Nse()
#print(nse.get_quote('infy'))
df = pd.read_csv('dta.csv')
#df = get_history(symbol='INFY',start=date(2013,12,25),end=date(2018,12,31))
print(df.columns.values)
df['Open'] = df['Open Price']
df['High'] = df['High Price']
df['Low'] = df['Low Price']
df['Close'] = df['Close Price']
#df['PCT_CHANGE'] = ((df['Open'] - df['Close'])/(df['Close']))*100
df = df[['Close','Open','High','Low']]
df['Label'] = df['Close'].shift(-3)
forecast_col = 'Close'
forecast_out = 3
df['Label'] = df[forecast_col].shift(-forecast_out)
#print(df[['CLose','label']])
X = np.array(df.drop(['Close','Label'],1))
# X - Features
# y - Labels

# X = preprocessing.scale(X)

X_lately = X[-forecast_out:]
X = X[:-forecast_out]

y = np.array(df['Label'])
y = y[:-forecast_out]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = LinearRegression()
clf.fit(X_train, y_train)
confidence = clf.score(X_test, y_test)  # coefficient of determination
print('confidence:', confidence)
forecast_set = clf.predict(X_lately)
# # print(df)
print(forecast_set)