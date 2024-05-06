from scipy.io import wavfile
import numpy as np

input_file ="C:/Users/Hrushi'/Documents/Computational lab/lab-8/Chorus.wav"
output_file = "C:/Users/Hrushi'/Documents/Computational lab/lab-8/wave.wav"

fs, y = wavfile.read(input_file)
reversedata = np.flipud(y)

wavfile.write(output_file, fs, reversedata)

