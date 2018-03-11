import os
import sys
import re

def tester(days=None,preset=None):
    if days==None:
        days=100
    if preset==None:
        preset=0
    models=os.listdir('../models')
    for model in models:
        if not(re.match(".*\.(py)",model)):
            continue
        model=model.split('.')[0]
        modeltester=open('models.txt','w')
        modeltester.write(model)
        print(model)
        os.system('python alltester.py '+str(days)+' '+str(preset))

if __name__=="__main__":
    days=None
    preset=None
    if len(sys.argv)>2:
        preset=int(sys.argv[2])
    if len(sys.argv)>1:
        days=int(sys.argv[1])
    tester(days,preset)
