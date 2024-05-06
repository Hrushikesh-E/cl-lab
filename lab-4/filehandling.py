import numpy as np
t=np.arange(0,1,0.01)
f=2
x=np.sin(2*np.pi*f*t)
#binary mode
f=open("sin2.bin","wb")
f.write(x)   
f.close()
f=open("sin2.bin","rb")
z=f.read()
print(z)
f.close()
#normal mode
f=open("sin1.txt","w")
f.write(str(x))
f.close()
f=open("sin1.txt","r")
z=f.read()
print(z)
f.close()
