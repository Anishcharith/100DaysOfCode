import numpy as np

def DCW(high,low,period):
    upperline=list(np.zeros(period))
    lowerline=list(np.zeros(period))
    DW=list(np.zeros(period))
    for i in range(period,len(high)):
        upperline.append(max(high[i-period:i]))
        lowerline.append(min(low[i-period:i]))
        DW.append(upperline[-1]-lowerline[-1])
    return upperline,lowerline,DW
