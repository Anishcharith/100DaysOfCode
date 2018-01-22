import sys
sys.path.insert(0,'../Day001/')
from SMA import SMA
import numpy as np

def LRF(close,period):
    sma=SMA(close,period)
    m=list(np.zeros(period))
    b=list(np.zeros(period))
    for i in range(period,len(close)):
        xavg=sma[i-1]
        yavg=sma[i]
        num=0
        dnum=0
        for j in range(period):
            num+=(close[i-j-1]-xavg)*(close[i-j]-yavg)
            dnum+=(close[i-j-1]-xavg)*(close[i-j-1]-xavg)
        m.append(num/dnum)
        b.append(yavg-m[i]*xavg)
    pred=[0]
    pred=[i*j+k for (i,j,k) in zip(close[1:],m[1:],b[1:])]
    return pred



