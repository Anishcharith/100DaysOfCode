import sys
import pandas as pd
import numpy as np
sys.path.insert(1,'../Day098/')
import niftygap
import matplotlib.pyplot as plt


if __name__=="__main__":
    period=100
    sma_period=200
    days=1000
    start=0
    comp=sys.argv[1]
    model_data=open(comp+'.txt')
    comp_data=pd.read_csv('../Data/'+comp+'.csv')
    close_p=np.flipud(comp_data['Close'].values[start:start+days])
    date=list(np.flipud(comp_data['Date'].values[start:start+days]))
    pl_vals=list(np.zeros(1000))
    rows=[]
    for row in model_data:
        if row.startswith("20"):
            rows.append(row.strip())
    print(rows)
    for i in range(0,len(rows),2):
        buy_date=rows[i-1].split('\t')[0]
        buy=float(rows[i].split('\t')[1])
        sell=float(rows[i-1].split('\t')[1])
        pl=(sell-buy)*100/buy
        index=date.index(buy_date)
        pl_vals[index]=pl
    print(len(pl_vals))
    plt.bar(np.arange(1000),pl_vals)
    niftygap.dispchart(close_p,sma_period,period)


