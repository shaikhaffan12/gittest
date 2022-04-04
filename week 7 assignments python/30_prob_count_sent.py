str = input("Enter A String To Count: ")
count_sent= 0
count_digits = 0
count_upper = 0
count_lower = 0

for i in str:
    if i.isnumeric():
        count_digits += 1

    if i.isalpha():
        count_sent += 1
        if i.isupper():
            count_sent += 1

        elif i.islower():
            count_lower += 1

print("Count Of Numbers: ",count_digits) 
print("Count Of Alphabets: ", count_sent)
print("Count Of UpperCase: ",count_upper)
print("Count Of LowerCase: ",count_lower)
