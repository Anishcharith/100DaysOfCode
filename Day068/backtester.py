import sys
import os
import numpy as np
import pandas as pd
from pipeliner import pipeliner

def main(comp,days):
    daysused=0
    daystate=0
    buystate=0
    buy_res=[]
    sell_res=[]
    date=[]
    i=0
    f=open(comp+'.txt','w')
    data=pd.read_csv('../Data/'+comp+'.csv')
    if days==None:
        days=len(data.index)
    close_p=np.flipud(data['Close'].values[0:days])
    open_p=np.flipud(data['Open'].values[0:days])
    low_p=np.flipud(data['Low'].values[0:days])
    high_p=np.flipud(data['High'].values[0:days])
    volume=np.flipud(data['Total Trade Quantity'].values[0:days])
    Date=np.flipud(data['Date'].values[0:days])
    buy_a,sell_a,stoploss_a=pipeliner(comp,days)

    while(i<len(buy_a)):
        if daystate:
            daysused+=1
        if buystate==0 and buy_a[i]==1:
            if daystate==0:
                daysused+=1
                daystate=1
            buystate=1
            date.append(Date[i])
            buy_res.append(close_p[i])
            f.write(str(date[-1])+"\t")
            f.write(str(buy_res[-1])+"\n")
        if buystate and (sell_a[i]==1 or stoploss_a[i]==1):
            daystate=0
            buystate=0
            date.append(Date[i])
            sell_res.append(close_p[i])
            f.write(str(date[-1])+"\t")
            f.write(str(sell_res[-1])+"\n")
            f.write("\n")
        i+=1
    if buystate==1:
        date.append(Date[-1])
        sell_res.append(close_p[-1])
        f.write(str(date[-1])+"\t")
        f.write(str(sell_res[-1])+"\n")
        f.write("\n")
    f.write("total Profit/Loss % : ")
    total=100*np.sum([(i-j)/(j+1) for (i,j) in zip(sell_res,buy_res)])
    f.write(str(total))
    print(comp+" : total Profit/Loss % : ",total,"days used :",daysused)
    f.close()
    return total,daysused


if __name__ == "__main__":
    comp=sys.argv[1]
    if len(sys.argv)>2:
        days=int(sys.argv[2])
    else:
        days=None
    main(comp,days)
