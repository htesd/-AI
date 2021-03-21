import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(-10, 10, 1000)
y = (1 / math.sqrt(2 * math.pi)) * np.exp(-x * x / 2)
plt.plot(x, y)
plt.show()
