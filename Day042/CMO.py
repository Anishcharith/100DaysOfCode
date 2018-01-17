import numpy as np

def CMO(close,period):
    cmo=list(np.zeros(period))
    for i in range(period,len(close)):
        su=0
        sd=0
        for j in range(i-period+1,i+1):
            if close[i]>close[i-1]:
                su+=close[i]-close[i-1]
            else:
                sd+=close[i-1]-close[i]
        cmo.append(100*(su-sd)/(su+sd))
    return cmo
