import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
sd='2014-07-18'
ed='2016-07-22'
dates=pd.date_range(sd,ed)
#print dates
#create empty dataframe
df1=pd.DataFrame(index=dates)
#print df1
#i="goog"
s= ["goldmansachs", "ibm" ]
dfSP=pd.read_csv("C:\\Users\\Abhishek\\Desktop\\Machine Learning for Trading\\aapl.csv",index_col= "Date", parse_dates = True, usecols=['Date','Close'], na_values = ['nan'])
dfSP=dfSP.rename(columns={'Close':"aapl"})
df1=df1.join(dfSP, how ="inner")
for i in s:
    dfSP1=pd.read_csv("C:\\Users\\Abhishek\\Desktop\\Machine Learning for Trading\\"+i + ".csv", 
    index_col="Date", parse_dates = True, usecols=["Date", "Close"], na_values = ['nan'] )
    dfSP1=dfSP1.rename(columns={'Close':i})
    df1=df1.join(dfSP1)
    df1=df1/df1.ix[0]
print df1    
df1.plot()   
mp.show()