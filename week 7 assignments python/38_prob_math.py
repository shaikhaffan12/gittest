class math_op:
    def add(self,a,b):
        res = a+b
        print(res)

    def sub(self,a,b):
        res = a-b
        print(res)

    def mul(self,a,b):
        res = a*b
        print(res)

    def div(self,a,b):
        res = a/b
        print(res)


obj = math_op()
obj.add(10,20)
obj.sub(20,30)
obj.mul(20,2)
obj.div(30,3)