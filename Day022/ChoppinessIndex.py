import sys
sys.path.insert(0,'../Day006')
import numpy as np
from ATR import ATR

def ChoppinessIndex(close,high,low,period=14):
    atr=ATR(close,high,low,1)
    CI=list(np.zeros(period-1))
    for i in range(period-1,len(close)):
        x=(100*np.log10(sum(atr[i-period+1:i])/((max(high[i-period+1:i])-min(low[i-period+1:i])))))
        CI.append(100*np.log10(sum(atr[i-period+1:i])/((max(high[i-period+1:i])-min(low[i-period+1:i]))))/np.log10(period))
    return CI
