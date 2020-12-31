# Writing a python extension

In this repository I have collected a few example of how to write an extension for python. In all example we will generate the [Madelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set) using the extension. This is a relatively computationally heavy algorithm which typically would be slow to write in pure python.

- [C extension using `ctypes`](ctypes_extension)
- [C++ extension using `pybind11`](pyvind11_extension)

In order to run all example you can install the conda environment that you can find the root directory of this repository

```
conda env create -f environment.yaml
```

Finally activate the environment

```
conda activate python_extensions
```