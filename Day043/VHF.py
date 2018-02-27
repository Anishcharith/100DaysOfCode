def VHF(close,period=28):
    HCP=[]
    LCP=[]
    sums=[close[0]]
    denum=[]
    for i in range(period-1):
        HCP.append(max(close[:i+1]))
        LCP.append(min(close[:i+1]))
        sums.append(abs(close[i]-close[i-1]))
        denum.append(sum(sums[:i+1]))
    for i in range(period-1,len(close)):
        HCP.append(max(close[i-period+1:i+1]))
        LCP.append(min(close[i-period+1:i+1]))
        sums.append(abs(close[i]-close[i-1]))
        denum.append(sum(sums[i-period+1:i+1]))
    VHF=[(i-j)/k for (i,j,k) in zip(HCP,LCP,denum)]
    return VHF
