input_file = "C:/Users/Hrushi'/Documents/Computational lab/lab-8/Chorus.wav"
output_file = "C:/Users/Hrushi'/Documents/Computational lab/lab-8/wave.wav"
[y,fs] = audioread(input_file);
reversedata = flipud(y);
audiowrite(output_file, reversedata, fs);
