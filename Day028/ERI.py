import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA

def ERI(close,high,low,period=13):
    ema=EMA(close,period)
    BullPower=[i-j for (i,j) in zip(high,ema)]
    BearPower=[i-j for (i,j) in zip(ema,low)]
    return BullPower,BearPower
