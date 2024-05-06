filepath = "C:/Users/Hrushi'/Downloads/Pop1.wav";
[s, fs] = audioread(filepath);
duration = length(s) / fs;  % Corrected the division operator
time = (0:length(s)-1) / fs;  % Corrected the division operator
plot(time, s);
title('pop1');

