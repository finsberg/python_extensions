
#include <pybind11/numpy.h>
#include <pybind11/pybind11.h>

#include <iostream>

namespace py = pybind11;

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

    double* xlin = new double[width];
    double* ylin = new double[height];
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

    delete[] xlin;
    delete[] ylin;
}

py::array_t<int> mandelbrot(double xmin, double xmax, double ymin, double ymax, int width, int height, int maxiter) {
    // constexpr int size = width * height;
    int* output = new int[width * height];

    mandelbrot_image(xmin, xmax, ymin, ymax,
                     width, height, maxiter, output);

    // Create a Python object that will free the allocated
    // memory when destroyed:
    py::capsule free_when_done(output, [](void* f) {
        int* output = reinterpret_cast<int*>(f);
        std::cerr << "Element [0] = " << output[0] << "\n";
        std::cerr << "freeing memory @ " << f << "\n";
        delete[] output;
    });

    return py::array_t<int>(
        {width, height},                      // shape
        {height * sizeof(int), sizeof(int)},  // C-style contiguous strides
        output,                               // the data pointer
        free_when_done);                      // numpy array references this parent
}

int main() {
    double xmin = -0.74877;
    double xmax = -0.74872;
    double ymin = 0.065053;
    double ymax = 0.065103;
    int width = 1000;
    int height = 1000;
    int maxiter = 2048;

    py::array_t<int> output = mandelbrot(xmin, xmax, ymin, ymax, width, height, maxiter);
    return 0;
}

PYBIND11_MODULE(mandelbrot_py, m) {
    m.doc() = "pybind11 mandelbrot ";

    m.def("mandelbrot", &mandelbrot, "Compute the mandelbrot image",
          py::arg("xmin"), py::arg("xmax"), py::arg("ymin"), py::arg("ymax"), py::arg("width"), py::arg("height"), py::arg("maxiter"));
}
