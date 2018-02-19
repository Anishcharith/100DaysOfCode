from operator import itemgetter
def order(file_name):
    data=open(file_name)
    comps={}
    comp_list=[]
    for row in data:
        x=row.split(':')
        temp=[]
        temp.append(x[0])
        temp.append(float(x[1]))
        temp.append(float(x[3]))
        comps[x[0]]=[float(x[1]),float(x[3])]
        comp_list.append(temp)
    comp_list.sort(key=itemgetter(2), reverse=True)
    print(comp_list)
    output_file=open('days_ordered_'+file_name,'w')
    for i in comp_list:
        output_file.write(i[0]+'\t\t\t\t'+str(i[1])+'\t\t\t\t'+str(i[2])+'\n')
    output_file.close()

order('100nifty50.txt')

