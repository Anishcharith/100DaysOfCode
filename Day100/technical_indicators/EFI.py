import sys
sys.path.insert(0,'../Day002/')
from EMA import EMA

def EFI(close,volume,period=14):
    efi1=[0]
    for i in range(1,len(close)):
        efi1.append((close[i]-close[i-1])*volume[i])
    EFI=EMA(efi1,period)
    return EFI
