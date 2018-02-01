import os
import sys
import pandas as pd
import numpy as np
comp=sys.argv[1]
# Technical indicators
sys.path.insert(0,'../Day004/')
sys.path.insert(0,'../Day007/')
from KeltnerChannel import KeltnerChannel
from BollingerBands import BB
# --------------------

def buy(open_p,close_p,low_p,high_p,volume):
    buy=[0]
    middle_line,upper_line,lower_line = KeltnerChannel(close_p,high_p,low_p,50,25,5)
    for i in range(1,len(close_p)):
        if close_p[i]>=upper_line[i]:
            buy.append(1)
        else:
            buy.append(0)
    return buy

def sell(open_p,close_p,low_p,high_p,volume):
    sell=[0]
    middle_line,upper_line,lower_line = KeltnerChannel(close_p,high_p,low_p,50,25,5)
    for i in range(1,len(close_p)):
        if close_p[i]<upper_line[i]:
            sell.append(1)
        else:
            sell.append(0)
    return sell

def stoploss(open_p,close_p,low_p,high_p,volume):
    stoploss=[0 for i in range(len(close_p))]
    return stoploss

def main(comp,days=None):
    data=pd.read_csv('../Data/'+comp+'.csv')
    if days==None:
        days=len(data.index)
    close_p=np.flipud(data['Close'].values[0:days])
    open_p=np.flipud(data['Open'].values[0:days])
    low_p=np.flipud(data['Low'].values[0:days])
    high_p=np.flipud(data['High'].values[0:days])
    volume=np.flipud(data['Total Trade Quantity'].values[0:days])
    buy_a=buy(open_p,close_p,low_p,high_p,volume)
    sell_a=sell(open_p,close_p,low_p,high_p,volume)
    stoploss_a=stoploss(open_p,close_p,low_p,high_p,volume)
    return buy_a,sell_a,stoploss_a

if __name__=="__main__":
    main(comp)
