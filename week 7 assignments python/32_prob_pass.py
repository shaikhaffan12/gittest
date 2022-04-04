
def psw(passsword):
    count = 0
    lst = ['@','#','$']

    if 6<= len(passsword) <=12:
        for i in passsword:
            if i.isnumeric():
                count +=1
                break

        for j in passsword:
            if j.isupper():
                count+=1
                break
    
        for k in passsword:
            if k.lower():
                count+=1
                break

        for l in passsword:
            if l in lst:
                count+=1
                break
   
        if count == 4:
            print("password is accepted: ",passsword)

        else:
            print("password is not acceped")

    else:
        print("password is too small or too big")


passsword1 =  input("Enter Password: ")
psw(passsword1)