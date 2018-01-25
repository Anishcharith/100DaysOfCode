import sys
sys.path.insert(0,'../Day002/')
sys.path.insert(0,'../Day006/')
from EMA import EMA
from ATR import ATR

def ADX(close,high,low,period=14):
    pdm=[0]
    ndm=[0]
    for i in range(1,len(close)):
        h=high[i]
        yh=high[i-1]
        l=low[i]
        yl=low[i-1]
        if h-yh>yl-l:
            pdm.append(h-yh)
            ndm.append(0)
        else:
            pdm.append(0)
            ndm.append(yl-l)
    expdm=EMA(pdm,period)       
    exndm=EMA(ndm,period)       
    atr=ATR(close,high,low,period)
    PDI=[100*i/(j+1) for (i,j) in zip(expdm,atr)]
    NDI=[100*i/(j+1) for (i,j) in zip(exndm,atr)]
    DX=[100*abs(i-j)/(i+j+1) for (i,j) in zip(PDI,NDI)]
    ADX=EMA(DX,period)
    return ADX,PDI,NDI
