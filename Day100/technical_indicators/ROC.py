import numpy as np

def ROC(close,period=14):
    roc=list(np.zeros(period))
    for i in range(period,len(close)):
        j=i-period
        roc.append((close[i]-close[j])*100/close[j])
    return roc
