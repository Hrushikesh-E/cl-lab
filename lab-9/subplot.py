import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0, 10.01, 0.01)
x = np.sin(0.5 * np.pi * t)
y = np.sin(0.5 * np.pi * t)
z = x + y

plt.figure()

plt.subplot(2, 3, 1)
plt.plot(x)

plt.subplot(2, 3, 2)
plt.plot(y)

plt.subplot(2, 3, 3)
plt.plot(z)

plt.show()

