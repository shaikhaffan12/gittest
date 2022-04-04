class mycls:
    def getstr(self, str1):
        print("The given String is :", str1)

    def printstr(self,str1):
        print('Here Is Your Upper Case Of String: ',str1.upper())

obj= mycls()

str2 = input('enter a string here: ')
obj.getstr(str2)
obj.printstr(str2)