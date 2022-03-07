lst = []
def even():
    
    for i in range(4,31):
        if i%2==0:
            lst.append(i)
    print(lst)

even()

# second solution

print(list(range(4,31,2)))