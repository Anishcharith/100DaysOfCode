import sys
import os
import numpy as np
import pandas as pd
import model1
import model2
#comp=sys.argv[2]

def main(comp,days):
    daysused=0
    daystate=0
    buystate_a=0
    buystate_b=0
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
    buy_a,sell_a,stoploss_a=model1.main(comp,days)
    buy_b,sell_b,stoploss_b=model2.main(comp,days)

    while(i<len(buy_a)):
        if daystate:
            daysused+=1
        if buystate_a==0 and buy_a[i]==1:
            daystate=1
            daysused+=1
            if buystate_b==1:
                buystate_a=1
                buystate_b=0
                continue
            buystate_a=1
            date.append(Date[i])
            buy_res.append(close_p[i])
            f.write(str(date[-1])+"\t")
            f.write(str(buy_res[-1])+"\n")
        elif buystate_b==0 and buystate_a==0 and buy_b[i]==1:
            daystate=1
            daysused+=1
            buystate_b=1
            date.append(Date[i])
            buy_res.append(close_p[i])
            f.write(str(date[-1])+"\t")
            f.write(str(buy_res[-1])+"\n")

        if (buystate_a and (sell_a[i]==1 or stoploss_a[i]==1)) or (buystate_b and (sell_b[i]==1 or stoploss_b[i]==1)) :
            daystate=0
            buystate_a=0
            buystate_b=0
            date.append(Date[i])
            sell_res.append(close_p[i])
            f.write(str(date[-1])+"\t")
            f.write(str(sell_res[-1])+"\n")
            f.write("\n")
        i+=1
    if buystate_a==1 or buystate_b==1:
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
    if len(sys.argv)>3:
        days=int(sys.argv[3])
    else:
        days=None
    main(comp,days)
