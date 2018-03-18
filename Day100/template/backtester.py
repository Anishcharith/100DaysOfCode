import sys
import os
import numpy as np
import pandas as pd
from pipeliner import pipeliner

def main(comp,days,start=0):
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
    close_p=np.flipud(data['Close'].values[start:start+days])
    open_p=np.flipud(data['Open'].values[start:start+days])
    low_p=np.flipud(data['Low'].values[start:start+days])
    high_p=np.flipud(data['High'].values[start:start+days])
    volume=np.flipud(data['Total Trade Quantity'].values[start:start+days])
    Date=np.flipud(data['Date'].values[start:start+days])
    buy_a,sell_a,stoploss_a=pipeliner(comp,days,start)

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
    if(buy_a[-1]==1):
        print("\n\t BUY today !! \n")
    f.close()
    return total,daysused


if __name__ == "__main__":
    comp=sys.argv[1]
    if len(sys.argv)>2:
        days=int(sys.argv[2])
    else:
        days=None
    if len(sys.argv)>3:
        start=int(sys.argv[3])
    else:
        start=0
    main(comp,days,start)
