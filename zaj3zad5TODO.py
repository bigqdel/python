import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
A = np.arange(2)
X, Y = np.meshgrid(A, A)
Z = X + Y
plt.imshow(Z, cmap='Blues',
interpolation='none')
plt.colorbar()
plt.show()