import numpy as np
import matplotlib.pyplot as plt
# Generate random signal x[n]
x = np.random.rand(1000)
# Calculate energy for every 20 amplitudes
energy = np.zeros(50)
for k in range(50):
    start_index = 20 * k
    end_index = min(20 * (k + 1), len(x))
    energy[k] = np.sum(np.abs(x[start_index:end_index])**2)
# Plot energy
plt.plot(energy)
plt.xlabel('Index k')
plt.ylabel('Energy e[k]')
plt.title('Energy for every 20 amplitudes')
plt.show()
