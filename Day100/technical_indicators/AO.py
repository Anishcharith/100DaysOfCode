import sys
sys.path.insert(0,'../Day016/')
from Aroon import Aroon

def AO(close,period):
    au,ad=Aroon(close,period)
    ao=[i-j for (i,j) in zip(au,ad)]
    print(au,ad)
    return ao
