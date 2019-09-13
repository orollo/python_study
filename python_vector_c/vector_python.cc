// vector_python.cpp
#include <vector>
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

extern "C" void foo(vector<int>* v, const char* FILE_NAME){
    string line;
    ifstream myfile(FILE_NAME);
    while (getline(myfile, line)) v->push_back(1);
}

extern "C" {
    vector<int>* new_vector(){
        return new vector<int>;
    }
    void delete_vector(vector<int>* v){
        cout << "destructor called in C++ for " << v << endl;
        delete v;
    }
    int vector_size(vector<int>* v){
        return v->size();
    }
    int vector_get(vector<int>* v, int i){
        return v->at(i);
    }
    void vector_push_back(vector<int>* v, int i){
        v->push_back(i);
    }
}
