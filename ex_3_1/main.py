#!/usr/bin/python3
from Vector import *
from ctypes import *


class DriverCallbacks(Structure):
    _fields_ = [
        ("func1",     c_void_p)
    ]


lib = cdll.LoadLibrary("./vector_python_lib.so")

# add function to list
a = Vector()
a.push(cast(lib.joons_func1, c_void_p))
a.push(cast(lib.joons_func2, c_void_p))


driverFuncList = DriverCallbacks()

# make function casting parameter
functype = CFUNCTYPE(c_void_p)

# cast integer to function pointer
func = functype(a[0])

# call function
func(pointer(driverFuncList))

