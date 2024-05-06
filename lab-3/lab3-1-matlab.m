t = 0:0.01:1;
sin_dict = containers.Map({'w1','w2','w3','w4','w5'}, {[1,2],[3,4],[3,6],[10,1],[1,3]});
disp('Choose: {''w1'':[1,2],''w2'':[3,4],''w3'':[3,6],''w4'':[10,1],''w5'':[1,3]}');
k = input('Enter sinusoidal key to generate:','s');
if isKey(sin_dict, k)
    x = sin_dict(k)(1) * sin(2 * pi * sin_dict(k)(2) * t);
    plot(t, x);
    xlabel('Time');
    ylabel('Amplitude');
    title(['wave: ' k]);
    grid on;
    legend('Signal');
else
    disp('Invalid key. Please choose a valid key from the dictionary.');
end

