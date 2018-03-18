import os
import backtester
import sys
import pandas as pd
days=int(sys.argv[1])

def main(days,start):
    NIFTY=pd.read_csv('ind_nifty50list.csv')
    NIFTYnse=NIFTY['Symbol'].values
    f=open(str(start)+':'+str(days)+'nifty50.txt','w')
    sumi=0
    totaldaysused=0
    for comp in NIFTYnse:
        result,daysused=backtester.main(comp,int(days),start)
        f.write(comp+':'+str(result)+':Days Used:'+str(daysused)+'\n')
        sumi+=result
        totaldaysused+=daysused
    print(sumi/50)
    print(totaldaysused/50)
    f.close()

if __name__=="__main__":
    if len(sys.argv)>2:
        start=int(sys.argv[2])
    else:
        start=0
    main(days,start)
