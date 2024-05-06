import numpy as np

t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
fp=open("numpy.npy","w")
np.savetxt(fp,x)
fp.close()
fp=open("numpy.npy","r")
data=np.loadtxt(fp)
print(data)
fp.close()