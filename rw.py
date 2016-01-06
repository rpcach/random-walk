#random walk

import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 1000, 0, 1])

y = .5

for i in range(1000):
    random = np.random.random()
    
    if random < .5:
        y -= .01
    else:
        y += .01
    
    plt.scatter(i, y)
    
plt.show()