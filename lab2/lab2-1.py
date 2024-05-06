import numpy as np
import matplotlib.pyplot as plt

x = float(input('Enter the start time: '))
y = float(input('Enter the end time: '))
t = np.arange(x, y + 0.01, 0.01)
freq = float(input('Enter the frequency: '))
w = np.sin(2 * np.pi * freq * t)
plt.title('Sine-wave')
plt.xlabel('t')
plt.ylabel('amp')
plt.plot(t, w)
plt.show()