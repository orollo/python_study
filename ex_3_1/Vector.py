#!/usr/bin/python3
from ctypes import *
#class DriverCallbacks(Structure):
#    _fields_ = [
#        ("func1",     c_void_p),
#        ("func2",    c_void_p),
#        ("func3", c_void_p)
#    ]
#

#extern "C" {
#    vector<func_p>* new_vector(){
#        return new vector<func_p>;
#    }
#    void delete_vector(vector<func_p>* v){
#        cout << "destructor called in C++ for " << v << endl;
#        delete v;
#    }
#    int vector_size(vector<func_p>* v){
#        return v->size();
#    }
#    func_p vector_get(vector<func_p>* v, int i){
#        return v->at(i);
#    }
#    void vector_push_back(vector<func_p>* v, func_p i){
#        v->push_back(i);
#    }
#}

class Vector(object):
    lib = cdll.LoadLibrary('./vector_python_lib.so') # class level loading lib
    lib.new_vector.restype = c_void_p
    lib.new_vector.argtypes = []
    lib.delete_vector.restype = None
    lib.delete_vector.argtypes = [c_void_p]
    lib.vector_size.restype = c_int
    lib.vector_size.argtypes = [c_void_p]
    lib.vector_get.restype = c_void_p
    lib.vector_get.argtypes = [c_void_p, c_int]
    lib.vector_push_back.restype = None
    lib.vector_push_back.argtypes = [c_void_p, c_void_p]
    lib.foo.restype = None
    lib.foo.argtypes = [c_void_p]

    def __init__(self):
        self.vector = Vector.lib.new_vector()  # pointer to new vector

    def __del__(self):  # when reference count hits 0 in Python,
        Vector.lib.delete_vector(self.vector)  # call C++ vector destructor

    def __len__(self):
        return Vector.lib.vector_size(self.vector)

    def __getitem__(self, i):  # access elements in vector at index
        if 0 <= i < len(self):
            return Vector.lib.vector_get(self.vector, c_int(i))
        raise IndexError('Vector index out of range')

#    def __repr__(self):
#        return '[{}]'.format(', '.join(str(self[i]) for i in range(len(self))))

    def push(self, i):  # push calls vector's push_back
        Vector.lib.vector_push_back(self.vector, i)#c_void_p(i))

    def foo(self, filename):  # foo in Python calls foo in C++
        Vector.lib.foo(self.vector, c_char_p(filename))
