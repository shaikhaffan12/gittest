
class mycomp:
    def __init__(self):
        self.str1 = input("Enter 1st string: ")
        self.str2 = input("Enter 2nd string: ")
    def compare(self):

        if len(self.str1)==len(self.str2):
            print(True)
        else:
            print(False)

obj = mycomp()
obj.compare()