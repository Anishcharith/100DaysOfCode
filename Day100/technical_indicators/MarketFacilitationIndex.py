def MarketFacilitationIndex(high,low,volume):
    mfi=[(i-j)/k for (i,j,k) in zip(high,low,volume)]
    terms=[0]
    for i in range(1,len(high)):
        if mfi[i]>mfi[i-1]:
            if volume[i]>volume[i-1]:
                terms.append('Green')
            else:
                terms.append('Squat')
        else:
            if volume[i]>volume[i-1]:
                terms.append('Fade')
            else:
                terms.append('Fake')
    return mfi,terms
