import numpy as np

def CMF(closep,lowp,highp,volume,period):
    mfm=[((c-l)-(h-c))/(h-l) for (h,l,c) in zip(highp,lowp,closep)]
    mfv=[i*j for (i,j) in zip(mfm,volume)]
    cmf=list(np.zeros(period-1))
    for i in range(period-1,len(mfv)):
        cmf.append(sum(mfv[i-period+1:i])/sum(volume[i-period+1:i]))
    return cmf
