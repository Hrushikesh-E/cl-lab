import numpy as num
from matplotlib import pyplot as plt
t=num.arange(0,10,0.1)
freq_1=10
sin1=num.sin(2*num.pi*freq_1*t)
freq_2=15
sin2=num.sin(2*num.pi*freq_2*t)
x=sin1+sin2
lw=int(input("enter the length of window:"))
y=num.zeros_like(t)
for n in range(len(t)):
	y[n]=num.sum(x[max(0,n-lw+1):n+1])
plt.plot(t,y,label='y[n]')
plt.xlabel('t')
plt.ylabel('amp')
plt.show()

