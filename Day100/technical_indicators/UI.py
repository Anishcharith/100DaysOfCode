import sys
sys.path.insert(0,'../Day001/')
import math
from SMA import SMA

def UI(close,period=14):
    HH=[]
    for i in range(period-1):
        HH.append(max(close[0:i+1]))
    for i in range(period-1,len(close)):
        HH.append(max(close[i-period+1:i+1]))
    pd=[100*(i-j)/j for (i,j) in zip(close,HH)]
    sa=SMA([i*i for i in pd],period)
    UI=[math.sqrt(i) for i in sa]
    return UI
