import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA
import numpy as np

def TMF(close,high,low,volume):
    HH=[high[0]]
    LL=[low[0]]
    for i in range(1,len(high)):
        HH.append(max(high[i],close[i-1]))
        LL.append(min(low[i],close[i-1]))
    num=EMA([i*(2*(j-k)/(l-k)-1) for (i,j,k,l) in zip(volume,close,LL,HH)],21)
    denum=EMA(volume,21)
    TMF=list(np.zeros(20))
    TMF+=[i/j for (i,j) in zip(num[20:],denum[20:])]
    return TMF
