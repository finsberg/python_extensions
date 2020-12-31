import numpy as np
import matplotlib.pyplot as plt
import numba


@numba.jit
def mandelbrot_pixel_numba(cx, cy, maxiter):
    x = cx
    y = cy
    for n in range(maxiter):
        x2 = x * x
        y2 = y * y
        if x2 + y2 > 4.0:
            return n
        y = 2 * x * y + cy
        x = x2 - y2 + cx
    return 0


@numba.jit(parallel=True)
def mandelbrot_parallel_numba(xmin, xmax, ymin, ymax, width, height, maxiter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))
    for i in numba.prange(width):
        for j in range(height):
            img[i, j] = mandelbrot_pixel_numba(x[i], y[j], maxiter)
    return img


if __name__ == "__main__":

    xmin = -2
    xmax = 0.5
    ymin = -1.25
    ymax = 1.25
    width = 1000
    height = 1000
    maxiter = 80

    img = mandelbrot_parallel_numba(xmin, xmax, ymin, ymax, width, height, maxiter)
    fig, ax = plt.subplots()
    q = ax.imshow(img.T, cmap="hot", origin="lower")
    ax.set_xticks(np.linspace(0, width, 5))
    ax.set_yticks(np.linspace(0, height, 5))
    ax.set_xticklabels(np.linspace(xmin, xmax, 5))
    ax.set_yticklabels(np.linspace(ymin, ymax, 5))
    ax.set_xlabel("Real axis")
    ax.set_ylabel("Imaginary axis")
    fig.colorbar(q)
    plt.show()
