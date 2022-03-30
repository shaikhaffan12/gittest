class diff:
    def diffrence(self):
        l=list(map(int,input("Enter array elements:").split(" ")))
        print(l)

        maximum = max(l)
        minimum = min(l)
        print("The diffrence is: ", maximum - minimum ) 


obj = diff()
obj.diffrence()


