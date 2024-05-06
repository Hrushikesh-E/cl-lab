x = input('Enter the start time: ');
y = input('Enter the end time: ');
t = x:0.01:y;
freq = input('Enter the frequency: ');
w = sin(2*pi*freq*t);
plot(t, w);
title('sine-wave');
xlabel('t');
ylabel('amp');
