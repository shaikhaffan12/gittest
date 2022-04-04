def sque(lst):
    lst1 = []
    for i in range(0,20):
        lst.append(i)

    for i in lst:
        if i%2 != 0:
            lst1.append(i**2)

    print(lst1)

lst = []
sque(lst)