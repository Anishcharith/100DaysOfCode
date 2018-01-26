import urllib.request
import pandas as pd
import os
import sys

comp=sys.argv[1]
try:
    urllib.request.urlretrieve('https://www.quandl.com/api/v3/datasets/NSE/'+comp+'.csv',filename='../Data/'+comp+'.csv')
    print(comp+' downloaded')
except:
    print('Couldnt get'+comp)




