duration=10;
t=linspace(0,duration,duration*100);
freq1=10;
sin1=sin(2*pi*freq1*t);
freq2=15;
sin2=sin(2*pi*freq2*t);
x=sin1+sin2;
lw=input('enter the length of window:');
y=zeros(size(t));
for n=1:length(t)
  y(n)=sum(x(max(1,n-lw+1):n));
end
plot(t,y,'display name','y[x]');
xlabel('t')
ylabel('amp')
