class mycmp:
    def __init__(self):
        self.num = int(input("Enetr A Number: "))

    def next(self):
        print("Next Number Is: ",self.num+1)

obj = mycmp()
obj.next()