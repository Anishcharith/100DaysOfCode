import numpy as np
import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA
def MassIndex(high,low,emaperiod=9,period=25):
    hl=[i-j for (i,j) in zip(high,low)]
    singleEMA=EMA(hl,emaperiod)
    doubleEMA=EMA(singleEMA,emaperiod)
    MI=list(np.zeros(period-1))
    EMAratio=list(np.zeros(period-1))
    EMAratio+=[i/j for (i,j) in zip(singleEMA[period-1:],doubleEMA[period-1:])]
    for i in range(period-1,len(high)):
        MI.append(sum(EMAratio[i-period+1:i]))
    return MI
