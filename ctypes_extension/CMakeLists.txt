cmake_minimum_required (VERSION 3.9 FATAL_ERROR)

project (ctypes_extension LANGUAGES C)

set(CMAKE_C_FLAGS_DEBUG "-g -Og -Wall")
set(CMAKE_C_FLAGS_RELEASE "-O3 -march=native")

set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${PROJECT_BINARY_DIR}/lib)

add_library(mandelbrot SHARED mandelbrot.c)
add_executable(mandelbrot_main mandelbrot.c)
install(TARGETS mandelbrot DESTINATION ${INVERSION_INSTALL_PYTHON_MODULE_DIR})

find_package(OpenMP)
if (OPENMP_FOUND)
    message("OpenMP was found")
    set(CMAKE_C_FLAGS_RELEASE "${CMAKE_C_FLAGS_RELEASE} ${OpenMP_C_FLAGS}")
    target_link_libraries(mandelbrot OpenMP::OpenMP_C)
    target_link_libraries(mandelbrot_main OpenMP::OpenMP_C)
else ()
    message("OpenMP was not found")
endif()
