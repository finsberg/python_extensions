# Writing a python extension

In this repository I have collected a few examples on how to write extensions for python. In all examples we will generate the [Madelbrot set](https://en.wikipedia.org/wiki/Mandelbrot_set). This is a relatively computationally heavy algorithm which typically would be slow to write in pure python.

- [C extension using `ctypes`](ctypes_extension)
- [C++ extension using `pybind11`](pyvind11_extension)
- [Rust extension using `PyO3` (TBW)](https://github.com/PyO3/pyo3)
- [C extension using `cffi` (TBW)](https://cffi.readthedocs.io/en/latest/)
- [Fortran extension using `f2py` (TBW)](https://www.numfys.net/howto/F2PY/)

We also compare with other methods such as 

- [Numba (jit compilation)](jit_compiled_numba)
- [Numpy vectorization](numpy_vectorization)
- [Pure python](pure_python)
- [Cython (TBW)](https://cython.org)
- [My (TBW)](https://github.com/python/mypy/tree/master/mypyc)

In order to run all example you can install the conda environment that you can find the root directory of this repository

```
conda env create -f environment.yaml
```

Finally activate the environment

```
conda activate python_extensions
```