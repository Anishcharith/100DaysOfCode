import sys
sys.path.insert(0,'../Day001/')
from SMA import SMA

def DPO(close,period=14):
    sma=SMA(close,period)
    shift=int(period/2)+1
    DPO=[i-j for (i,j) in zip(close[:-shift],sma[shift:])]
    return DPO
