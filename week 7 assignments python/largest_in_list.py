def maximum():
    num = int(input("Enter A number: "))
    lst = []
    maxi = 0

    for i in range(num):
        ele = int(input("enter element of list: "))
        lst.append(ele)

    print(lst)

    for data in lst:
        if data > maxi:
            maxi = data

    print(maxi) 

maximum()


