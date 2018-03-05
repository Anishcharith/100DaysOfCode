import urllib.request
import pandas as pd
import os
tryagain=[]
NIFTY=pd.read_csv('ind_nifty50list.csv')
NIFTYnse=NIFTY['Symbol'].values
os.system('mkdir -p ../Data/')
for comp in NIFTYnse:
    try:
        urllib.request.urlretrieve('https://www.quandl.com/api/v3/datasets/NSE/'+comp+'.csv',filename='../Data/'+comp+'.csv')
        print(comp+' done')
    except:
        tryagain.append(comp);
        print('Couldnt get '+comp)
while(tryagain!=[]):
    temp=[]
    print("trying again")
    for comp in tryagain:
        try:
            urllib.request.urlretrieve('https://www.quandl.com/api/v3/datasets/NSE/'+comp+'.csv',filename='../Data/'+comp+'.csv')
            print(comp+' done')
        except:
            temp.append(comp);
            print('Couldnt get '+comp)
    tryagain=[]
    tryagain=temp[:]
    temp=[]
