import sys
sys.path.insert(0,'../Day006/')
from ATR import ATR
import numpy as np
import math

def RWI(close,high,low,period):
    RWIhigh=list(np.zeros(period))
    RWIlow=list(np.zeros(period))
    for i in range(period,len(close)):
        rwihigh=0
        rwilow=0
        for j in range(1,period):
            atr=ATR(close[i-j:i+1],high[i-j:i+1],low[i-j:i+1],j+1)[-1]
            x=(high[i]-low[i-j])/(atr*math.sqrt(j+1))
            rwihigh=max(rwihigh,x)
            y=(high[i-j]-low[i])/(atr*math.sqrt(j+1))
            rwilow=max(rwilow,y)
        RWIhigh.append(rwihigh)
        RWIlow.append(rwilow)
    return RWIhigh,RWIlow


