class mycmp:
    def __init__(self):
        self.num = int(input("Enter A number: "))
    def div_by(self):
        if self.num%5==0:
            print(True)

        else:
            print(False)

obj = mycmp()
obj.div_by()

