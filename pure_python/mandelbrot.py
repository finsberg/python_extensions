import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_pixel(c, maxiter):
    """Check wether a single pixel diverges"""
    z = 0

    for n in range(maxiter):
        z = z * z + c
        if abs(z) > 2:
            return n

    return 0


def mandelbrot_image(xmin, xmax, ymin, ymax, width, height, maxiter):
    """Render an image of the Mandelbrot set"""
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i, xi in enumerate(x):
        for j, yj in enumerate(y):
            c = xi + 1j * yj
            img[i, j] = mandelbrot_pixel(c, maxiter)

    return img


if __name__ == "__main__":

    xmin = -2
    xmax = 0.5
    ymin = -1.25
    ymax = 1.25
    width = 1000
    height = 1000
    maxiter = 80
    img = mandelbrot_image(xmin, xmax, ymin, ymax, width, height, maxiter)
    fig, ax = plt.subplots(dpi=300)
    q = ax.imshow(img.T, cmap="hot", origin="lower")
    ax.set_xticks(np.linspace(0, width, 5))
    ax.set_yticks(np.linspace(0, height, 5))
    ax.set_xticklabels(np.linspace(xmin, xmax, 5))
    ax.set_yticklabels(np.linspace(ymin, ymax, 5))
    ax.set_xlabel("Real axis")
    ax.set_ylabel("Imaginary axis")
    fig.colorbar(q)
    plt.show()
