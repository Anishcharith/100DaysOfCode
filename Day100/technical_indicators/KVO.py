import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA

def KVO(close,high,low,volume,period=13,shortperiod=34,longperiod=55):
    keyprice=[(i+j+k)/3 for (i,j,k) in zip(close,high,low)]
    trend=[0]
    for i in range(1,len(close)):
        if keyprice[i]>keyprice[i-1]:
            trend.append(volume[i])
        else:
            trend.append(-volume[i])
    emashort=EMA(trend,shortperiod)
    emalong=EMA(trend,longperiod)
    KVO=[i-j for (i,j) in zip(emashort,emalong)]
    KVOsignal=EMA(KVO,period)
    return KVO,KVOsignal
