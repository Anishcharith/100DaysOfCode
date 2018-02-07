import sys
import numpy as np
sys.path.insert(0,'../Day002')
from EMA import EMA

def PVO(volume,shortperiod=12,longperiod=26):
    emashort=EMA(volume,shortperiod)
    emalong=EMA(volume,longperiod)
    pvo=list(np.zeros(longperiod-1))
    for i in range(longperiod-1,len(emalong)):
        pvo.append(100*(emashort[i]-emalong[i])/emalong[i])
    return pvo
