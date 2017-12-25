import sys
sys.path.insert(0,'../Day018/')
sys.path.insert(0,'../Day002/')
from EMA import EMA
from ROC import ROC

def CoppockCurve(close,shortRocPeriod=11,longRocPeriod=14,period=10):
    shortRoc=ROC(close,shortRocPeriod)
    longRoc=ROC(close,longRocPeriod)
    CC=EMA([i+j for (i,j) in zip(shortRoc,longRoc)],period)
    return CC
