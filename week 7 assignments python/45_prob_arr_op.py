class mycls:
    def rem_at(self,list1,ind):
        x=list1.pop(ind)
        print(list1)

    def ins_at(self,list1):
        y=list1.insert(3,22)
        print(list1)

    def ins_at_last(self,list1,val):
        z=list1.append(val)
        print(list1)


obj = mycls()
list1 = [54, 44, 27, 79, 91, 41]
val = 33
ind = 2
obj.rem_at(list1,ind)

obj.ins_at_last(list1,val)
