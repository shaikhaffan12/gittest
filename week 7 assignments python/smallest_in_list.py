def minimum():
    num = int(input("Enter A number: "))
    lst = []
    

    for i in range(num):
        ele = int(input("enter element of list: "))
        lst.append(ele)

    print(lst)
    mini = lst[0]

    for data in range(1,len(lst)):
        if lst[data] < mini:
            mini = lst[data]

    print(mini) 


minimum()