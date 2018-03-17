import os
import sys
import pandas as pd
import numpy as np
sys.path.insert(0,'../Day001/')
from SMA import SMA
import matplotlib.pyplot as plt

def dispchart(close_p,sma_period=200,period=100):
    sma=SMA(close_p,sma_period)
    diff=[(close_p[i]-sma[i])/close_p[i] for i in range(len(close_p))]
    print(len(diff))
    gap=list(np.zeros(period))
    gap+=[sum(diff[i-period:i+1]) for i in range(period,len(close_p))]
    plt.plot(np.arange(1000),gap)
    plt.axvline(period+sma_period,color='red')
    plt.axhline(0,color='black')
    plt.axvline(0,color='black')
    plt.show()
    return gap

def getclose(comp,days=None,start=0):
    data=pd.read_csv('../Data/'+comp+'.csv')
    if days==None:
        days=len(data.index)
    close_p=np.flipud(data['Close'].values[start:start+days])
    return close_p


if __name__=="__main__":
    comp=sys.argv[1]
    close_p=getclose(comp,2000)
    sma_period=200
    period=100
    try:
        sma_period=sys.argv[2]
    except:
        pass
    try:
        period=sys.argv[3]
    except:
        pass
    dispchart(close_p,sma_period,period)



    

    
