import soundfile as sf
from matplotlib import pyplot as plt

filepath = "C:/Users/Hrushi'/Documents/Computational lab/lab-7/Pop1.wav"
signal, sample_rate = sf.read(filepath)
time = [i / sample_rate for i in range(len(signal))]

plt.figure(figsize=(10, 4))
plt.plot(time, signal)  # Plot the signal
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Audio Signal')
plt.show()
