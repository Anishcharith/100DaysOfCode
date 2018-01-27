import sys
import os
import numpy as np
import pandas as pd
import model
comp=sys.argv[2]

def main():
    buystate=0
    buy_res=[]
    sell_res=[]
    buy_a,sell_a,stoploss_a=model.main(comp)
    date=[]
    i=0
    f=open('result.txt','w')
    data=pd.read_csv('../Data/'+comp+'.csv')
    close_p=np.flipud(data['Close'].values)
    open_p=np.flipud(data['Open'].values)
    low_p=np.flipud(data['Low'].values)
    high_p=np.flipud(data['High'].values)
    volume=np.flipud(data['Total Trade Quantity'].values)
    Date=np.flipud(data['Date'].values)

    while(i<len(buy_a)):
        if buystate==0 and buy_a[i]==1:
            buystate=1
            date.append(Date[i])
            buy_res.append(close_p[i])
            f.write(str(date[-1])+"\t")
            f.write(str(buy_res[-1])+"\n")
        if buystate and (sell_a[i]==1 or stoploss_a[i]==1):
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
    print("total Profit/Loss % : ",total)
    f.close()


if __name__ == "__main__":
    main()
