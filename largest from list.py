def large():
    x= [4,6,8,24,12,2,89,34,66,49]
    large = 0
    for i in x:
        if i>large:
            large=i
    return large


largest = large()
print(largest)