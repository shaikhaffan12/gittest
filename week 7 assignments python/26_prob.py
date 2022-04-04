from ntpath import join

def myfunc(lst):
    
    for i in range(2000,4700):
        if i%7 == 0 and i%5 != 0:
            lst.append(str(i))


lst1 = [] 
myfunc(lst1)
print(','.join(lst1))