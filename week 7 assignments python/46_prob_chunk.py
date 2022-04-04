sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89] 

def chunk(list):
    first = list[0:3]
    second = list[3:6]
    third = list[6:9]
    print(first[::-1])
    print(second[::-1])
    print(third[::-1])

chunk(sample_list)


