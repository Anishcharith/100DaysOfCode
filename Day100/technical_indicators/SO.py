def SO(close,high,low,period=14):
    Lows=[]
    Highs=[]
    SO=[]
    for i in range(period-1):
        Lows.append(min(low[:i+1]))
        Highs.append(max(high[:i+1]))
    for i in range(period-1,len(close)):
        Lows.append(min(low[i-period+1:i+1]))
        Highs.append(max(high[i-period+1:i+1]))
    for i in range(len(close)):
        SO.append(100*(close[i]-Lows[i])/(Highs[i]-Lows[i]))
    return SO
