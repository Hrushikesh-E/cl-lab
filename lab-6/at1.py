import numpy as np
import matplotlib.pyplot as plt
x=[]
x1=int(input("enter length:"))
for i in range(x1):
	f=float(input("enter x[n]:"))
	x.append(f)
y1=int(input("enter len of y[k]:"))
k=np.arange(1,y+0.01,0.01)
y=np.zeros_like(x1)
for i in range(x1):
	y+=x[i]*np.cos(2*np.pi*i*k)
plt.plot(k,y)
plt.show