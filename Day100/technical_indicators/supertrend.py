import sys
sys.path.insert(0,'../Day006/')
from ATR import ATR

def supertrend(close,high,low,period=7,multiplier=3):
    atr=ATR(close,high,low,period)
    basic_upper=[(i-j)/2+multiplier*k for (i,j,k) in zip(high,low,atr)]
    basic_lower=[(i-j)/2-multiplier*k for (i,j,k) in zip(high,low,atr)]
    final_upper=[basic_upper[0]]
    final_lower=[basic_lower[0]]
    for i in range(1,len(close)):
        if basic_upper[i]<final_upper[-1] or close[i-1]>final_upper[-1] :
            final_upper.append(basic_upper[i])
        else:
            final_upper.append(final_upper[-1])

        if basic_lower[i]>final_lower[-1] or close[i-1]<final_lower[-1] :
            final_lower.append(basic_lower[i])
        else:
            final_lower.append(final_lower[-1])
    strend=[]
    for i in range(len(close)):
        if close[i]<=final_upper[i]:
            strend.append(final_upper[i])
        else:
            strend.append(final_lower[i])

    return strend
