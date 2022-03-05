num1 = 10
num2 = 0

try:
    res = num1/num2
    num3 = int(input("enter a integer number\n"))
except ZeroDivisionError:
    print("cannot divide bye zero")

except ValueError:
    print("please provide a number")

except:
    print("something went wrong")

finally:
    print("thank you!!")