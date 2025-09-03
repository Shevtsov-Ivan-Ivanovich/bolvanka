%matplotlib inline

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 2, 4, 5, 6, 1 , 4, 2, 5 ])
ypoints = np.array([0, 250, 140, 220, 22, 241, 123, 123, 22])
zpoints = np.array([1, 3, 4, 4, 6, 2, 5, 7])
plt.plot(xpoints, ypoints)
plt.show()


