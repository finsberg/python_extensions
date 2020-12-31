cmake_minimum_required (VERSION 3.9 FATAL_ERROR)
project(mandelbrot LANGUAGES CXX)

set(CMAKE_CXX_FLAGS_DEBUG "-g -Og -Wall")
set(CMAKE_CXX_FLAGS_RELEASE "-O3 -march=native")

find_package(pybind11 REQUIRED)
pybind11_add_module(mandelbrot_py mandelbrot.cpp)
