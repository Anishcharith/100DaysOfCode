def PSAR(close):
    state=1                                         # 1 if uptrend, 0 if downtrend
    ep=close[0]
    SAR=[close[0]]
    af=0.02
    for i in range(1,len(close)):
        if SAR[i-1]>close[i-1] and state==1:
            state=0
            af=.02
            ep=close[i-1]
        if SAR[i-1]<close[i-1] and state==0:
            state=1
            af=.02
            ep=close[i-1]
        SAR.append(SAR[i-1]+af*(ep-SAR[i-1]))
        if state==1 and close[i]>ep:
            ep=close[i]
            af+=.02
        if state==0 and close[i]<ep:
            ep=close[i]
            af+=.02
    return SAR
