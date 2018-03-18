import sys
sys.path.insert(0,'../Day001/')
from SMA import SMA

def EOM(high,low,volume,period=14):
    DM=[0]
    for i in range(1,len(high)):
        DM.append((high[i]+low[i])/2-(high[i-1]-low[i-1])/2)
    BR=[(v/100000000)/(h-l) for (v,h,l) in zip(volume,high,low)]
    EOM1=[d-b for (d,b) in zip(DM,BR)]
    EOM=SMA(EOM1,period)
    return EOM
