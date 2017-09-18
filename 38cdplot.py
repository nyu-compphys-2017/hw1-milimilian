#3.8 parts c and d#

import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt("C:/Users/MNK/Desktop/millikan.txt", float)
x = data[:,0]
y = data[:,1]
y1 = np.empty(6, float)
m = 4.08822735852e-15  
c = -1.73123580398
i = 0
for i in range(6):
    y1[i] = m*x[i] + c
    i += 1

print("The value of planck's constant is e*m =", 1.602e-19*m,"J.s")#the value of Planck's constant#
print("the accuracy is about:", 1.2, "%")
plt.plot(x, y, "ko")
plt.plot(x, y1)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage (volt)")
plt.xlim(-2.0e+14, 1.5e+15)
plt.show()



