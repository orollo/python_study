#!/usr/bin/python3
from ctypes import *

#load the shared object file
adder = CDLL('./add.so')## DLL을 읽어옴 

#Find sum of integers
res_int = adder.add_int(4,5)
print("Sum of 4 and 5 = " + str(res_int))

#Find sum of floats
a = c_float(5.5)## ctypes에 정의된 float 
b = c_float(4.1)

add_float = adder.add_float
add_float.restype = c_float
print("Sum of 5.5 and 4.1 = ", str(add_float(a, b)))

