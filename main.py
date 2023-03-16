import numpy as np
import matplotlib.pyplot as plt

x = np.random.random_sample((4, ))
y = np.random.random_sample((4, ))

div = 100

nCPTS = np.size(x, 0)
n = nCPTS - 1
i = 0
t = np.linspace(0, 1, div)
b = []

xBesier = np.zeros((1, div))
yBesier = np.zeros((1, div))


# binomial coefficient
def Ni(n, i):
    return np.math.factorial(n) / np.math.factorial(i) / np.math.factorial(n - i)

# Bernstein basis polynomial
def basisFunction(n, i, t):
    J = np.array(Ni(n, i) * (t ** i) * (1 - t) ** (n - i))
    return J

for k in range(0, nCPTS):
    b.append(basisFunction(n, i, t))

    xBesier = basisFunction(n, i, t) * x[k] + xBesier
    yBesier = basisFunction(n, i, t) * y[k] + yBesier
    i += 1


fig1 = plt.figure(figsize=(4, 4))
ax1 = fig1.add_subplot(111)
ax1.scatter(x, y, c='black')
ax1.plot(xBesier[0], yBesier[0], c='blue')

plt.grid(False)
plt.axis('off')


plt.show()