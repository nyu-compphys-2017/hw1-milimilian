#problem 3.7 (Mandelbrot set with 1000*1000 grid system and 300 iterations#
import numpy as np
import matplotlib.pyplot as plt

a = np.empty([1000, 1000], float)
x = np.linspace(-2, 2, 1000)
y = np.linspace(-2, 2, 1000)

def mand(ite, c):
	z = 0
	i = 0
	for i in range(ite):
		z = z**2 + c
		i += 1
		if np.abs(z) > 2:
			return ite
	return 0

k = q = 0
for k in range(1000):
	for q in range(1000):
		a[q, k] = mand(300, x[k] + y[q]*1j)
		q+=1
	k = k + 1
	q = 0

plt.imshow(a, origin="lower", extent=[-2,2,-2,2])
plt.gray()
plt.show()
