import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA
import numpy as np

def TRIX(close,period):
    tripleema=EMA(EMA(EMA(close,period),period),period)
    trix=list(np.zeros(period))
    for i in range(period,len(close)):
        trix.append(100*(tripleema[i]-tripleema[i-1])/tripleema[i-1])
    return trix
