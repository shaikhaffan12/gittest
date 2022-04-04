
class mycls:
    def ind_at(self):
        nest= [[1,2,'jack'],[3,4,'sorrow']]
        add_list = [5,6,'john']
        ind = int(input("Enter Index: "))
        nest.insert(ind,add_list)
        print(nest)


obj = mycls()
obj.ind_at()