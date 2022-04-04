class divide:
    def __init__(self):
        self.num1 = int(input("Enter first number: "))
        self.num2 = int(input("Enter second number: "))
    def div(self):
        if self.num1%self.num2 == 0:
            print(True)
        else:
            print(False)

obj = divide()
obj.div()