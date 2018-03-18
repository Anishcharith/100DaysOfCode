import os
import sys
import pandas as pd
import numpy as np
# Technical indicators
sys.path.insert(0,'../technical_indicators/')
from GAPO import GAPO
from PSAR import PSAR
# --------------------

def buy(open_p,close_p,low_p,high_p,volume):
    buy=[0]
    gapo=GAPO(high_p,low_p)
    sar=PSAR(close_p)
    for i in range(1,len(close_p)):
        if gapo[i]<1 and sar[i]<close_p[i] :
            buy.append(1)
        else:
            buy.append(0)
    return buy

def sell(open_p,close_p,low_p,high_p,volume):
    sell=[0]
    sar=PSAR(close_p)
    for i in range(1,len(close_p)):
        if sar[i]>close_p[i]:
            sell.append(1)
        else:
            sell.append(0)
    return sell

def stoploss(open_p,close_p,low_p,high_p,volume):
    stoploss=[0 for i in range(len(close_p))]
    return stoploss

def main(comp,days=None,start=0):
    data=pd.read_csv('../Data/'+comp+'.csv')
    if days==None:
        days=len(data.index)
    close_p=np.flipud(data['Close'].values[start:start+days])
    open_p=np.flipud(data['Open'].values[start:start+days])
    low_p=np.flipud(data['Low'].values[start:start+days])
    high_p=np.flipud(data['High'].values[start:start+days])
    volume=np.flipud(data['Total Trade Quantity'].values[start:start+days])
    buy_a=buy(open_p,close_p,low_p,high_p,volume)
    sell_a=sell(open_p,close_p,low_p,high_p,volume)
    stoploss_a=stoploss(open_p,close_p,low_p,high_p,volume)
    return buy_a,sell_a,stoploss_a

if __name__=="__main__":
    comp=sys.argv[1]
    main(comp)
