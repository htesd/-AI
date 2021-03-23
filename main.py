import numpy as np
from matplotlib import pyplot as plt
import math

x = np.arange(-6, 6, 0.01)



def normalF(x, mu=0, sigma=1):
    a = 1 / (math.sqrt(2 * math.pi) * sigma)
    b = math.exp(-math.pow(x - mu, 2) / (2 * math.pow(sigma, 2)))

    return a * b


plt.title("Normal function")

# y = normalF(x)
y = [normalF(t) for t in x]
plt.plot(x, y)
plt.show()
