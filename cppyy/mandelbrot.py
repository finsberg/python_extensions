import numpy as np
import matplotlib.pyplot as plt
import cppyy

cppyy.include("vector")

cppyy.cppdef(
    """
int mandelbrot_pixel(double cx, double cy, int maxiter)
{
    double x = cx;
    double y = cy;

    for (int n = 0; n < maxiter; n++) {
        double x2 = x * x;
        double y2 = y * y;

        if (x2 + y2 > 4.0) {
            return n;
        }

        y = 2 * x * y + cy;
        x = x2 - y2 + cx;
    }
    return 0;
}

void mandelbrot_image(double xmin, double xmax, double ymin, double ymax, int width, int height,
                      int maxiter, std::vector<int> &output)
{
    int i, j;

    double xlin[width];
    double ylin[height];
    double dx = (xmax - xmin) / width;
    double dy = (ymax - ymin) / width;

    for (i = 0; i < width; i++) {
        xlin[i] = xmin + i * dx;
    }

    for (j = 0; j < height; j++) {
        ylin[j] = ymin + j * dy;
    }

    for (i = 0; i < width; i++) {
        // #pragma omp parallel for
        for (j = 0; j < height; j++) {
            output[i * height + j] = mandelbrot_pixel(xlin[i], ylin[j], maxiter);
        }
    }
}

std::vector<int> mandelbrot(double xmin, double xmax, double ymin, double ymax, int width,
                            int height, int maxiter)
{
    // constexpr int size = width * height;
    std::vector<int> output(width * height);

    mandelbrot_image(xmin, xmax, ymin, ymax, width, height, maxiter, output);

    return output;
}

"""
)

from cppyy.gbl import mandelbrot

xmin = -0.74877
xmax = -0.74872
ymin = 0.065053
ymax = 0.065103
width = 1000
height = 1000
maxiter = 2048

output = mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter)
output = np.array(output).reshape((width, height))

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
