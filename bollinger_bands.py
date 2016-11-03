import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
sd='2000-01-18'
ed='2016-10-22'
dates=pd.date_range(sd,ed)
#create empty dataframe
df1=pd.DataFrame(index=dates)
rm1=pd.DataFrame(index=dates)
s= [ "snp"]
for i in s:
    dfSP1=pd.read_csv("C:\\Users\\Abhishek\\Desktop\\Machine Learning for Trading\\"+ i + ".csv", 
    index_col="Date", parse_dates = True, usecols=["Date", "Close"])
    dfSP1=dfSP1.rename(columns={'Close':i})
    df1=df1.join(dfSP1)
    ax=df1[i].plot(title = 'Bollinger Bands')
    ax.plot( label="Goldman sachs" )
    r_mean=df1[i].resample("2D").ffill(limit=0).rolling(window=50, min_periods=1).mean()
    r_mean.plot(label = "Simple Moving Average")
    r_sd=df1[i].resample("2D").ffill(limit=0).rolling(window=50, min_periods=1).std()
    upper_band=r_mean + 2 * r_sd
    lower_band=r_mean - 2 * r_sd
    upper_band.plot(label = "Upper Band")
    lower_band.plot(label = "Lower Band")
    #rm1=rm1.join(upper_band)
    #rm1=rm1.join(lower_band)
    #for normalization
   #df1=df1/df1.ix[0]
ax.set_xlabel('Date',fontsize=14)
ax.set_ylabel('Price',fontsize=14)
ax.legend(loc='lower right')
mp.show()
#mp.show()  