import pandas as pd
import matplotlib.pyplot as mp
import numpy as np
import warnings
warnings.simplefilter('ignore',np.RankWarning )
'''edit the date range as per your analysis requirement'''
sd='2015-01-01'
ed='2016-08-12'
dates=pd.date_range(sd,ed)
#create empty dataframe
df1=pd.DataFrame(index=dates)
s= [ "snp", "ibm","goldmansachs"]
for i in s:
    #change the name of the directory below which contains your csv file for stock data
    dfSP1=pd.read_csv("C:\\Users\\Abhishek\\Desktop\\Machine Learning for Trading\\"+ i + ".csv", 
    index_col="Date", parse_dates = True, usecols=["Date", "Close"], na_values='nan')
    dfSP1=dfSP1.rename(columns={'Close':i})
    df1=df1.join(dfSP1)
    '''computing daily returns'''
    drns=df1.copy()
    drns[1:]=(df1[1:]/df1[:-1].values) - 1
    drns.ix[0,:]=0
    #ax=drns.plot(title = 'S&P 500', label = "Daily Returns" )
''' filling missing values'''

drns.fillna(method='ffill',inplace='TRUE')
drns.fillna(method='bfill',inplace='TRUE')    

'''plotting daily returns'''
#to be fixed and debugged
#drns['snp'].plot(title = 'S&P 500', label = "Daily Returns" )
#mp.legend(loc = 'upper right') 
#drns['ibm'].plot(title = 'IBM', label = "Daily Returns" )
#mp.legend(loc = 'upper right') 
#drns['goldmansachs'].plot(title = 'Goldman Sachs', label = "Daily Returns" )
#mp.legend(loc = 'upper right') 

''' plotting histogram'''    

drns['snp'].hist(bins=40, label='snp')
drns['ibm'].hist(bins=40, label='ibm')
drns['goldmansachs'].hist(bins=40, label='goldmansachs')
mean = drns.mean()
std =  drns.std() 
mp.legend(loc = 'upper right')   
#mp.axvline(mean + std,color = 'r', linestyle='dashed',linewidth=2) #AXVLINE function not working

''' plotting scatterplot and linear regression '''

drns.plot(kind = 'scatter', x='snp', y='ibm', label='Scatter Plots')
beta_IBM, alpha_IBM= np.polyfit(drns['snp'],drns['ibm'],1)
mp.plot(drns['snp'], beta_IBM * drns['snp'] + alpha_IBM,'-', color='g', label = 'Linear Regression')
print "IBM"
print beta_IBM,alpha_IBM 
mp.legend(loc = 'lower right')
drns.plot(kind = 'scatter', x='snp', y='goldmansachs', label='Scatter Plots')
beta_gs, alpha_gs= np.polyfit(drns['snp'],drns['goldmansachs'],1)
mp.plot(drns['snp'], beta_gs * drns['snp'] + alpha_gs, '-',color='r', label = 'Linear Regression')
print "goldmansachs"
print beta_gs,alpha_gs 
mp.legend(loc = 'lower right')

'''additional plotting functionalities'''

#ax.set_xlabel('Date',fontsize=14)
#ax.set_ylabel('Price',fontsize=14)
#ax.legend(loc='lower right')
#print drns.kurtosis()
mp.show()
  