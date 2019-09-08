#!/usr/bin/python3


def func1(data):
    print(f"func data {data}")

def func2(data):
    print(f"func2 data {data}")



if __name__ == "__main__":

    lists = []
    lists.append(func1)
    lists.append(func2)
    lists.append(func2)
    lists.append(func1)


    i = 0

    for l in lists:
        i = i + 1
        l(i)


