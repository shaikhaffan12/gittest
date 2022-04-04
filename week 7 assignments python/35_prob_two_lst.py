class mycls:
    def str_len(self,str1,str2):
        if len(str1) == len(str2):
            print(str1, end='\n')
            print(str2)

str1 = input("enter first string: ")
str2 = input("enter second string: ")

obj=mycls()
obj.str_len(str1,str2)