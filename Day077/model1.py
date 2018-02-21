import os
import sys
import pandas as pd
import numpy as np
# Technical indicators
sys.path.insert(0,'../Day041/')
sys.path.insert(0,'../Day050/')
from WR import WR
from ADX import ADX
# --------------------

def buy(open_p,close_p,low_p,high_p,volume):
    buy=[0]
    wr=WR(close_p,high_p,low_p)
    adx,pdi,ndi=ADX(close_p,high_p,low_p)
    for i in range(1,len(close_p)):
        if wr[i]>-20 :
            buy.append(1)
        else:
            buy.append(0)
    return buy

def sell(open_p,close_p,low_p,high_p,volume):
    sell=[0]
    wr=WR(close_p,high_p,low_p)
    for i in range(1,len(close_p)):
        if wr[i-1]>-20:
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
