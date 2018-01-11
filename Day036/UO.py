import numpy as np

def UO(close,high,low):
    BP=[close[0]-low[0]]
    TR=[high[0]-low[0]]
    for i in range(1,len(close)):
        BP.append(close[i]-min(low[i],close[i-1]))
        TR.append(max(high[i],close[i-1])-min(low[i],close[i-1]))
    avg7=list(np.zeros(6))
    avg7+=[sum(BP[i-6:i+1])/sum(TR[i-6:i+1]) for i in range(6,len(BP))]
    avg14=list(np.zeros(13))
    avg14+=[sum(BP[i-13:i+1])/sum(TR[i-13:i+1]) for i in range(13,len(BP))]
    avg28=list(np.zeros(27))
    avg28+=[sum(BP[i-27:i+1])/sum(TR[i-27:i+1]) for i in range(27,len(BP))]
    UO=[100*(4*i+2*j+k)/7 for (i,j,k) in zip(avg7,avg14,avg28)]
    return UO
