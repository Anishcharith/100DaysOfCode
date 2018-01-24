import sys
sys.path.insert(0,'../Day006/')
sys.path.insert(0,'../Day001/')
from SMA import SMA
from ATR import ATR

def STARC(close,high,low,period=15,maperiod=5,multiplier=1.33):
    ma=SMA(close,maperiod)
    atr=ATR(close,high,low,period)
    upperband=[i+j*multiplier for (i,j) in zip(ma,atr)]
    lowerband=[i-j*multiplier for (i,j) in zip(ma,atr)]
    return upperband,lowerband
