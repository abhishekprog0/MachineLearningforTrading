import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import warnings
warnings.simplefilter('ignore',np.RankWarning )
sd='2015-01-01'
ed='2016-08-12'
dates=pd.date_range(sd,ed)
#create empty dataframe
df1=pd.DataFrame(index=dates)
#drns=pd.DataFrame(index=dates)
s= [ "snp", "ibm","goldmansachs"]
for i in s:
    dfSP1=pd.read_csv("C:\\Users\\Abhishek\\Desktop\\Machine Learning for Trading\\"+ i + ".csv", 
    index_col="Date", parse_dates = True, usecols=["Date", "Close"], na_values='nan')
    dfSP1=dfSP1.rename(columns={'Close':i})
    df1=df1.join(dfSP1)
    drns=df1.copy()
    drns[1:]=(df1[1:]/df1[:-1].values) - 1
    drns.ix[0,:]=0
    #ax=drns.plot(title = 'S&P 500', label = "Daily Returns" )
''' filling missing values'''

drns.fillna(method='ffill',inplace='TRUE')
drns.fillna(method='bfill',inplace='TRUE')    

''' plotting histogram'''    

drns['snp'].hist(bins=40, label='snp')
drns['ibm'].hist(bins=40, label='ibm')
m = drns.mean()
std =  drns.std()    
mp.axvline(m,color = 'w', linestyle='dashed',linewidth=2)
''' plotting scatterplot and linear regression '''
#mp.subplot(211)
drns.plot(kind = 'scatter', x='snp', y='ibm')
beta_IBM, alpha_IBM= np.polyfit(drns['snp'],drns['ibm'],1)
print "IBM"
print beta_IBM,alpha_IBM 
mp.plot(drns['snp'], beta_IBM * drns['snp'] + alpha_IBM,'-', color='g')
#mp.subplot(212)
drns.plot(kind = 'scatter', x='snp', y='goldmansachs')
beta_gs, alpha_gs= np.polyfit(drns['snp'],drns['goldmansachs'],1)
print "goldmansachs"
print beta_gs,alpha_gs 
mp.plot(drns['snp'], beta_gs * drns['snp'] + alpha_gs, '-',color='r')
#ax.set_xlabel('Date',fontsize=14)
#ax.set_ylabel('Price',fontsize=14)
#ax.legend(loc='lower right')
#print drns.kurtosis()
mp.legend(loc = 'upper right')
mp.show()
#mp.show()  