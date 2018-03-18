def PVI(close,volume):
    PVI=[volume[0]]
    for i in range(1,len(close)):
        if volume[i]<volume[i-1]:
            PVI.append(PVI[-1])
        else:
            PVI.append(PVI[-1]+PVI[-1]*(close[i]-close[i-1])/close[i-1])
    return PVI
