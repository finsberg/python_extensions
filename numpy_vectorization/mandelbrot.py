import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_numpy(xmin, xmax, ymin, ymax, width, height, maxiter):
    x = np.linspace(xmin, xmax, num=width).reshape((1, width))
    y = np.linspace(ymin, ymax, num=height).reshape((height, 1))
    C = np.tile(x, (height, 1)) + 1j * np.tile(y, (1, width))

    Z = np.zeros((height, width), dtype=complex)
    M = np.ones((height, width), dtype=bool)
    M_tmp = np.ones((height, width), dtype=bool)
    img = np.zeros((height, width), dtype=float)
    for i in range(maxiter):
        Z[M] = Z[M] * Z[M] + C[M]
        M[np.abs(Z) > 2] = False
        M_tmp = ~M & ~M_tmp
        img[~M_tmp] = i
        M_tmp[:] = M[:]

    img[np.where(img == maxiter - 1)] = 0
    return img.T


if __name__ == "__main__":
    xmin = -2
    xmax = 0.5
    ymin = -1.25
    ymax = 1.25
    width = 1000
    height = 1000
    maxiter = 80
    img = mandelbrot_numpy(xmin, xmax, ymin, ymax, width, height, maxiter)
    fig, ax = plt.subplots(dpi=150)
    q = ax.imshow(img.T, cmap="hot", origin="lower")
    ax.set_xticks(np.linspace(0, width, 5))
    ax.set_yticks(np.linspace(0, height, 5))
    ax.set_xticklabels(np.linspace(xmin, xmax, 5))
    ax.set_yticklabels(np.linspace(ymin, ymax, 5))
    ax.set_xlabel("Real axis")
    ax.set_ylabel("Imaginary axis")
    fig.colorbar(q)
    plt.show()
