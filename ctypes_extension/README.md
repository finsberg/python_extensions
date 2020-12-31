# C extension using `ctypes`

`ctypes` is library that is part of the python standard library so there is no need to install any third party packages to use `ctypes`. However, in this example we will use `numpy` arrays as well as matplotlib for plotting. You also need `CMake` in order to build the shared library.

## Build shared library
```
mkdir -p build
cd build
cmake ..
make 
```
