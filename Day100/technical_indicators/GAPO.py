import math
import sys
sys.path.insert(0,'../Day025/')
from DCW import DCW
import numpy as np

def GAPO(high,low,period=14):
   hh,ll,d=DCW(high,low,period) 
   GRI=list(np.zeros(period))
   GRI+=[math.log(i-j)/math.log(period) for (i,j) in zip(hh[period:],ll[period:])]
   return GRI
