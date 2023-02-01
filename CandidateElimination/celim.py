import numpy as np
import pandas as pd
data=pd.read_csv("climate.csv")
concepts=np.array(data.iloc[:,0:-1])
print ("Instances are : \n",concepts)
target=np.array(data.iloc[:,-1])
print ("Target values are: \n",target)
def learn(concepts,target):
    specific=concepts[0].copy()
    print ("Initialization of specific and general")
    print ("specific boundary: ",specific)
    general=[["?" for i in range(len(specific))]for j in range(len(specific))]
    print ("general boundary: ",general)
    for i,h in enumerate(concepts):
        print ("\ninstance",i+1,"is",h)
        if target[i]=="yes":
            print("instance is positive")
            for x in range(len(specific)):
                if h[x]!=specific[x]:
                    specific[x]='?'
                    general[x][x]='?'
        if target[i]=="no":
            print("instance is negative")
            for x in range(len(specific)):
                if h[x]!=specific[x]:
                    general[x][x]=specific[x]
                else:
                    general[x][x]='?'
        print("specific boundary after ",i+1," instance is ",specific)
        print("general boundary after ",i+1," instance is ",general)
    indices=[i for i,val in enumerate(general) if val==['?','?','?','?','?','?']]
    for i in indices:
        general.remove(['?','?','?','?','?','?'])
    return specific,general
s_final,g_final=learn(concepts,target)
print("final specific: ",s_final,sep="\n")
print("final general: ",g_final,sep="\n")