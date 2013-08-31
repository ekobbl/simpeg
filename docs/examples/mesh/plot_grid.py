import numpy as np
import matplotlib.pyplot as plt
from SimPEG import TensorMesh

x0 = np.zeros(2)
h1 = np.linspace(.1,.5,3)
h2 = np.linspace(.1,.5,5)
mesh = TensorMesh([h1,h2],x0)
mesh.plotGrid()

plt.show()

