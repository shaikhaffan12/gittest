num_of_animals = int(input("enter number of animals: "))
legs = 0

if num_of_animals > 0:
    num_of_chic = int(input("enter number of chckens: "))
    num_of_cows = int(input("enter number of cows: "))
    num_of_pigs = int(input("enter number of pigs: "))
    if num_of_chic > 0:
        for i in range(num_of_chic):
            legs += 2

    if num_of_cows > 0 :
        for i in range(num_of_cows):
            legs += 4

    if num_of_pigs > 0:
        for i in range(num_of_pigs):
            legs += 4 
    print("The Number Of legs: ", legs)
else:
    print("please give correct number for animals.")

