#!/usr/bin/python3
def square(i):
        result = i;
        for x in range(i-1):
                result *= i

        return result

def calculate(func, a, b):
        return func(a+b);

def main():
        print (calculate(square, 1, 1))

if __name__ == "__main__":
    main()

