import pandas as pd
import numpy as np
import re
            
def find(c):
    sp=[]
    a=df['name'].values.tolist()                                 # Converting dataframe column in to list

    d=c.split(' ')
    d.reverse()
    
    for z in range(len(c),(len(c)-int(len(d[len(d)-1])/2)),-1):  # for checking whether the input string is similar to the begining of the strings in the list
        for zp in a:
            x = re.search("^%s"%c[:z],zp)
            if x:
                if zp not in sp:
                    sp.append(zp)            
    flag=0
    for i in d:
        for j in range(len(i),3,-1):
            if flag==0:
                for zp in a:
                    x = re.search("%s$"%i[:j],zp)        # for checking whether the input string is similar to the end of the strings in the list
                    if x:
                        if zp not in sp:
                            sp.append(zp)               
            else:
                for o in a:                             # for checking whether the input string is present anywhere in the strings of the list
                        if i[:j] in o:
                            if zp not in sp:
                                sp.append(zp)                                         
        flag=flag+1
    if (len(sp)>=20):                                 # for printing the top 20 searches
        for i in range(0,20):
            print(sp[i])
    elif (len(sp)==0):
        print("Found Nothing")
    else:
        for i in range(0,len(sp)):
            print(sp[i])
if __name__ == '__main__':            
    df=pd.read_csv('python_assesment.csv')
    c=input().upper()
    find(c)
