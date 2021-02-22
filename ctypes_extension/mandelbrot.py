"""
"""
import sys

# import os
from pathlib import Path
from ctypes import c_double, c_int

import numpy as np
import matplotlib.pyplot as plt

# In case you have multiple copies of libomp,
# see https://stackoverflow.com/questions/53014306/error-15-initializing-libiomp5-dylib-but-found-libiomp5-dylib-already-initial
# os.environ["KMP_DUPLICATE_LIB_OK"] = "True"

here = Path(__file__).absolute().parent
libdir = here.joinpath("build").joinpath("lib")

try:
    libfile = next(f for f in libdir.iterdir() if f.stem == "libmandelbrot")
except StopIteration:
    print("Please generate shared lib file for mandelbrot")
    sys.exit(1)

lib = np.ctypeslib.load_library(libfile, here)

# Create 2D array of int pointer
float64_array_2d = np.ctypeslib.ndpointer(dtype=c_int, ndim=2, flags="contiguous")
# Arguments to the mandelbrot function
lib.mandelbrot.argtypes = [
    c_double,  # xmin
    c_double,  # xmax
    c_double,  # ymin
    c_double,  # ymax
    c_int,  # width
    c_int,  # height
    c_int,  # maxiter
    float64_array_2d,  # output
]
# Return type is void
lib.mandelbrot.restype = None



# Allocate array to be filled

def mandelbrot_image(xmin, xmax, ymin, ymax, width, height, maxiter):
    output = np.zeros((width, height), dtype=np.int32)
    lib.mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter, output)
    return output


if __name__ == "__main__":

    xmin = -0.74877
    xmax = -0.74872
    ymin = 0.065053
    ymax = 0.065103
    width = 1000
    height = 1000
    maxiter = 2048
    
    output = mandelbrot_image(xmin, xmax, ymin, ymax, width, height, maxiter)
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
