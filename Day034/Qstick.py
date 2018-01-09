import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA

def Qstick(closep,openp,period):
    diff=[i-j for (i,j) in zip(closep,openp)]
    Qstick=EMA(diff,period)
    return Qstick
