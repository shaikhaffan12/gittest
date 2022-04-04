def evenly(n):

    lst = []
    for i in range(n):
        if i%2==0:
            lst.append(i)

    print(",".join(map(str,lst)))

numm = int(input("enter a number for finding even number: "))
evenly(numm)