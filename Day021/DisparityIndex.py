import numpy as np
import sys
sys.path.insert(0,'../Day001/')
from SMA import SMA

def DI(close,period=14):
    DI=list(np.zeros(period-1))
    sma=SMA(close,period)
    DI+=[(i-j)*100/j for (i,j) in zip(close[period-1:],sma[period-1:])]
    return DI
