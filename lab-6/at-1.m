x=[]
x1=input('enter length of array:')
y=0
for i=1:x1
  f=input('enter x[n]:')
  x=[x,f];
end
y1=input('enter length of y[k]:')
k=1:0.1:y1
for i =1:x1
  y+=x(i)*cos(2*pi*i*k)
end
plot(y)
