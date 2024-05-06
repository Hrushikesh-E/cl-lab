import numpy as np
from matplotlib import pyplot as plt
t=np.arange(0,1,0.01)
sin_dict={'w1':[1,2],'w2':[3,2],'w3':[1,6],'w4':[3,6],'w5':[1,5]}

print("choose: {'w1':[1,2],'w2':[3,2],'w3':[1,6],'w4':[3,6],'w5':[1,5]}") 

k=input("Enter sinusoidal key to generate:")

if sin_dict[k]:
    x=sin_dict[k][0]*np.sin(2*np.pi*sin_dict[k][1]*t)
    plt.plot(t,x)
    plt.show()