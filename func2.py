from re import I


def func1(*args):
    print("printing values\n")
    for i in args:
        print(i)

func1(10,20,30,40,50)