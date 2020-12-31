"""
"""
import sys

sys.path.insert(0, "build")

import numpy as np
import matplotlib.pyplot as plt

import mandelbrot_py

xmin = -0.74877
xmax = -0.74872
ymin = 0.065053
ymax = 0.065103
width = 1000
height = 1000
maxiter = 2048

output = mandelbrot_py.mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter)

# Plot solution
fig, ax = plt.subplots(dpi=150)
q = ax.imshow(output.T, cmap="hot", origin="lower")
ax.set_xticks(np.linspace(0, width, 3))
ax.set_yticks(np.linspace(0, height, 3))
ax.set_xticklabels(np.linspace(xmin, xmax, 3))
ax.set_yticklabels(np.linspace(ymin, ymax, 3))
ax.set_xlabel("Real axis")
ax.set_ylabel("Imaginary axis")
fig.colorbar(q)
plt.show()
