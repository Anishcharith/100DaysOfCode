import os
import backtester
import sys
import pandas as pd
days=sys.argv[1]

def main(days):
    NIFTY=pd.read_csv('ind_nifty50list.csv')
    NIFTYnse=NIFTY['Symbol'].values
    f=open(str(days)+'nifty50.txt','w')
    sumi=0
    totaldaysused=0
    for comp in NIFTYnse:
        result,daysused=backtester.main(comp,int(days))
        f.write(comp+':'+str(result)+':Days Used:'+str(daysused)+'\n')
        sumi+=result
        totaldaysused+=daysused
    print(sumi/50)
    print(totaldaysused/50)
    f.close()

if __name__=="__main__":
    main(days)
