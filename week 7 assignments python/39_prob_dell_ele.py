class mycls:
    def dell_ele():
        listi = [12,24,35,70,88,120,155,99,12,7,8,93,67,47,76,34,43,76,23,1]
        remove_ele = [0,4,5]

        for i in remove_ele:
         del listi[i]

        print(listi)

obj = mycls()
obj.dell_ele()