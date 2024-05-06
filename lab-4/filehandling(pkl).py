import numpy as np
import pickle
t=np.arange(0,1,0.01)
f=5
x=np.sin(2*np.pi*f*t)
fp=open("sin_pickle.pkl","wb")
pickle.dump(x,fp)
fp.close()

fp=open("sin_pickle.pkl","rb")
k=pickle.load(fp)
print(k)
fp.close()