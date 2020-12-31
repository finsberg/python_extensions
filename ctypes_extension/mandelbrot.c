#include <stdlib.h>

int mandelbrot_pixel(double cx, double cy, int maxiter) {
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

void mandelbrot_image(double xmin, double xmax,
                      double ymin, double ymax,
                      int width, int height,
                      int maxiter, int* output) {
    int i, j;

    double* xlin = malloc(width * sizeof(double));
    double* ylin = malloc(height * sizeof(double));

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

    free(xlin);
    free(ylin);
}
void mandelbrot(double xmin, double xmax, double ymin, double ymax, int width, int height, int maxiter, int* output) {
    mandelbrot_image(xmin, xmax, ymin, ymax,
                     width, height, maxiter, output);
}

int main() {
    double xmin = -0.74877;
    double xmax = -0.74872;
    double ymin = 0.065053;
    double ymax = 0.065103;
    int width = 1000;
    int height = 1000;
    int maxiter = 2048;

    int* output = malloc(width * height * sizeof(int));

    mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter, output);
    free(output);

    return 0;
}