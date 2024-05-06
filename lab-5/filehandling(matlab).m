t = 0:0.01:1;
f =3;
x = sin(2*pi*f*t);
fid = fopen('matlab.txt', 'wt');
fprintf(fid, '%f\n', x);
fclose(fid);
fid = fopen('matlab.txt', 'rt');
x_read = fscanf(fid, '%f');
fclose(fid);
plot(t, x_read);
xlabel('t');
ylabel('x');
title('Plot of x vs. t');

