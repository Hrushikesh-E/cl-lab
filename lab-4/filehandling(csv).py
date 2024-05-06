import csv
import numpy as np
t=np.arange(0,1,0.01)
freq=5
x=np.sin(2*np.pi*freq*t)
np.savetxt('csv.csv',x,delimiter=",")  
f=open("csv.csv","r")
k=f.read()
print(k)
f.close()
