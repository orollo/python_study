#!/usr/bin/python3


def func1(i):
    print(f"this is number: {i}")

def func2(i):
    print(f"this is func2: {i}")

def func3(i):
    print(f"this is func3: {i}")


def search(lists, name, value):
    for item in lists:
        if item["name"] == name:
            item["func"](value)




if __name__ == "__main__":

    # list
#    lists = [{"name":"func1", "func": func1},
#            {"name":"func2", "func": func2},
#            ]

    lists = []

    lists.append({"name":"func3", "func": func3})
    print (type(lists))

    

    print(type(lists))

    search(lists, "func1", 4)
    search(lists, "func2", 9)
    search(lists, "func3", 15)


