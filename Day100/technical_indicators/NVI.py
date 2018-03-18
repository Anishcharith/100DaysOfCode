def NVI(close,volume):
    NVI=[volume[0]]
    for i in range(1,len(close)):
        if volume[i]>volume[i-1]:
            NVI.append(NVI[i-1])
        else:
            NVI.append(NVI[-1]+NVI[-1]*(close[i]-close[i-1])/close[i-1])
    return NVI
