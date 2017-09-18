#3.8 part a#

import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt("C:/Users/MNK/Desktop/millikan.txt", float)
x = data[:,0]
y = data[:,1]
plt.plot(x, y, "ko")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage (volt)")
plt.xlim(-1.0e+14, 1.5e+15)
plt.ylim(-0.5, 4)
plt.show()


