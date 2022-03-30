class mycomp:
    def __init__(self):
        self.lst = [24,45,67,89,90]
        self.res = 0
    def last_ele(self):
        for i in self.lst:
            self.res += i

        print(self.res)

obj = mycomp()
obj.last_ele()