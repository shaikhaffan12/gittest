from dataclasses import replace

class mycls:
    def replace_alpha(self,str1):
        x= str1.replace("a","z")
        print(x)

    def replace_word(self,txt):
        x = txt.replace("apple", "banana")
        print(x)

obj = mycls()
str2 = input("enter a string: ")
obj.replace_alpha(str2)
obj.replace_word(str2)
