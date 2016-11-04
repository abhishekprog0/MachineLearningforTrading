import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import warnings
warnings.simplefilter('ignore',np.RankWarning )
investment = 1000000
'''alpha is the weights assigned to each stock in the portfolio'''
alpha = [0.1,0.1,0.8]
'''edit the date range as per your analysis requirement'''
sd='2013-01-01'
ed='2014-08-12'
dates=pd.date_range(sd,ed)
#create empty dataframe
df=pd.DataFrame(index=dates)
'''you can add more company to the stocks list'''
stocks= [ "snp", "goog","goldmansachs"]
for i in stocks:
    
    '''reading stock data from the csv file download from yahoo.finance'''
    #change the name of the directory below which contains your csv file for stock data
    df_temp=pd.read_csv("C:\\Users\\Abhishek\\Desktop\\Machine Learning for Trading\\"+ i + ".csv", 
    index_col="Date", parse_dates = True, usecols=["Date", "Close"], na_values='nan')
    df_temp=df_temp.rename(columns={'Close':i})
    df=df.join(df_temp)
    
    ''' filling missing values'''
    df.fillna(method='ffill',inplace='TRUE')
    df.fillna(method='bfill',inplace='TRUE') 
    
    '''normalization'''
    df=df/df.ix[0]
    
'''building the portfolio'''
df['snp']=df['snp']*alpha[0] 
df['goog']=df['goog']*alpha[1]
df['goldmansachs']=df['goldmansachs'] * alpha[2]
df=df * investment
df=df.sum(axis=1)
print df

'''calculating portfolio statistics'''
'''computing daily returns'''
drns=df.copy()
drns[1:]=(df[1:]/df[:-1].values) - 1
drns.ix[0]=0  
drns=drns[1:]
#returns=df[-1]/df[0] * 100  #technical issues    
mean=drns.mean()
std=drns.std()
k=15.8745
sharpe_ratio=k * (mean/std)
print "Portfolio Statistics: "
#print "returns: ", returns,"%"
print "sharpe ratio: ", sharpe_ratio

'''plotting the portfolio returns from the investment'''
ax=df.plot(title = 'Portfolio Analysis')
ax.set_xlabel('Date')
ax.set_ylabel('Portfolio Price')
mp.show()
    