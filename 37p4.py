#Problem 3.7 Mandelbrot jet colored set in terms of number of iteration#
#500*500 grid system with maximum 200 iterations#
import numpy as np
import matplotlib.pyplot as plt

a = np.empty([500, 500], float)
x = np.linspace(-2, 2, 500)
y = np.linspace(-2, 2, 500)

def mand(ite, c):
	z = 0
	i = 0
	for i in range(ite):
		z = z**2 + c
		i += 1
		if np.abs(z) > 2:
			return i
	return ite

k = q = 0
for k in range(500):
	for q in range(500):
		a[q, k] = mand(200, x[k] + y[q]*1j)
		q+=1
	k = k + 1
	q = 0

plt.imshow(a, origin="lower", extent=[-2,2,-2,2])
plt.jet()
plt.show()



