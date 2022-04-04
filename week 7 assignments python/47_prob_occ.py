list1 = [11, 45, 8, 11, 23, 45, 23, 45, 89]

dict1 = {}

for i in list1:
    if dict1.get(i):
        dict1[i] += 1
    else:
        dict1[i] = 1

print(dict1)

