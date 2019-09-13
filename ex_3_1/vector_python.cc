// vector_python.cpp
#include <vector>
#include <iostream>
#include <fstream>
#include <string>
typedef void(*func_p)(void*);
typedef struct DriverCallbacks_t
{
    func_p                func1;
} DriverCallbacks;



using namespace std;

extern "C" void joons_func1(void*)
{
    printf("joons!, first\n");
}

extern "C" void joons_func2(void*)
{
    printf("joons!, second\n");
}


extern "C" void foo(vector<func_p>* v, const char* FILE_NAME){
    v->push_back(&joons_func1);
}

extern "C" {
    vector<func_p>* new_vector(){
        return new vector<func_p>;
    }
    void delete_vector(vector<func_p>* v){
        cout << "destructor called in C++ for " << v << endl;
        delete v;
    }
    int vector_size(vector<func_p>* v){
        return v->size();
    }
    func_p vector_get(vector<func_p>* v, int i){
        return v->at(i);
    }
    void vector_push_back(vector<func_p>* v, func_p i){
        v->push_back(i);
    }
}
