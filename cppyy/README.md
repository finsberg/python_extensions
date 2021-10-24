# Automatic Python-C++ bindings using `cppyy`

In this demo we will demonstrate how to use [`cppyy`](https://cppyy.readthedocs.io/en/latest/index.html)

Do do this you first need to install `cppyy`
```
python -m pip install cppyy
```

We will use `vector` as container for the data. To include this we need to tell `cppyy` this using the following line
```python
import cppyy

cppyy.include("vector")
```

To define a c++ function you can use `cppyy.cppdef`, for example

```python
cppyy.cppdef("""
int magic_number(){
    return 42;
}
""")
```
Now we can import the function in python
```python
>>> from cppyy.gbl import magic_number
>>> magic_number()
42
```
See [mandelbrot.py](mandelbrot.py) for the mandelbrot demo.
