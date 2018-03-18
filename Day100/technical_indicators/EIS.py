import sys
sys.path.insert(0,'../Day002')
sys.path.insert(0,'../Day003')
from EMA import EMA
from MACD import MACD

def EIS(close):
    eis=[]
    macd,signal,histogram=MACD(close)
    eis.append('b')
    ema13=EMA(close,13)
    for i in range(1,len(close)):
        if ema13[i]>ema13[i-1] and histogram[i]>histogram[i-1]:
            eis.append('g')
        elif ema13[i]<ema13[i-1] and histogram[i]<histogram[i-1]:
            eis.append('r')
        else:
            eis.append('b')
    return eis
