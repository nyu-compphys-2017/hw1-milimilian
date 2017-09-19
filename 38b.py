#3.8 part b#

import numpy as np
import matplotlib.pyplot as plt
import math

data = np.loadtxt("C:/Users/MNK/Desktop/millikan.txt", float)
x = data[:,0]
y = data[:,1]
i = 0
Ex = Ey = Exx = Exy = 0
for i in range(x.size):
    Ex += (1/x.size)*x[i]
    Ey += (1/x.size)*y[i]
    Exx += (1/x.size)*(x[i]**2)
    Exy += (1/x.size)*(x[i]*y[i])
    i += 1

m = (Exy - Ex*Ey)/(Exx - Ex**2)
c =  (Exx*Ey - Ex*Exy)/(Exx - Ex**2)
print(" the slope and intercept are:", m,"and", c)

plt.plot(x, y, "ko")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Voltage (volt)")
plt.xlim(-1.0e+14, 1.5e+15)
plt.ylim(-0.5, 4)
plt.show()
