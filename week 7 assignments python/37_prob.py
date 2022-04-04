input_str = input("enter the string: ")
list1 = input_str.split(' ')

lst1=[]
lst2=[]

for i in list1:
    if i.isnumeric():
        lst1.append(i)
print(lst1)

for i in list1:
    if i.isalpha():
        lst2.append(i)
print(lst2)