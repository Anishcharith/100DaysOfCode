import importlib
import numpy as np

def pipeliner(comp,days):
    model_names=open('models.txt','r')
    models=[]
    buy=list(np.zeros(int(days)))
    sell=list(np.zeros(days))
    sl=list(np.zeros(days))
    for model in model_names:
        model=model.rstrip()
        buystate=0
        models.append(importlib.import_module(model))
        buy_b,sell_b,sl_b=models[-1].main(comp,days)
        for i in range(len(buy_b)):
            if buystate==1:
                continue
            if buy[i]==1:
                if buystate==0:
                    buystate=1
                else :
                    buy[i]=0
                    buystate=1
                continue
            if buystate==1 and sell[i]==1 :
                buystate=0
            if buystate==1 and sl[i]==1 :
                buystate=0
            if buystate==0 and buy_b[i]==1:
                buy[i]=1
                buystate=2
            if buystate==2 and sell_b[i]==1 :
                buystate=0
                sell[i]=1
            if buystate==2 and sl_b[i]==1 :
                buystate=0
                sl[i]=1
    return buy,sell,sl
