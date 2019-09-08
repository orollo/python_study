#include <stdio.h>

int add_int(int, int);
float add_float(float, float);

int add_int(int num1, int num2){
    printf("C: add int: %d, %d\n", num1, num2);
    return num1 + num2;
}

float add_float(float num1, float num2){
    return num1 + num2;
}

