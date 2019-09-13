g++ -c -fPIC vector_python.cpp -o vector_python.o
g++ -shared -Wl,-install_name,vector_python_lib.so -o vector_python_lib.so vector_python.o
