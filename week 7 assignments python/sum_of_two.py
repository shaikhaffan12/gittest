class summation:
    def __init__(self):
        self.a = int(input("Enter 1st NUmber: "))
        self.b = int(input("Enter 2nd NUmber: "))

    def summ(self):
        result = self.a + self.b
        print(result)

obj = summation()
obj.summ()
