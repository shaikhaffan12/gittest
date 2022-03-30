class module:
    def __init__(self,num1, num2):
        self.num1 = num1
        self.num2 = num2

    def modulo(self):
        print("The Remainder is: ",self.num1 % self.num2)

obj = module(19,2)
obj.modulo()
