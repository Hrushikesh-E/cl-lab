t=0:0.01:10
x=sin(0.5*pi*t)
y=cos(0.5*pi*t)
z=x+y
figure()
subplot(2,3,1)
plot(x)
subplot(2,3,2)
plot(y)
subplot(2,3,3)
plot(z)
