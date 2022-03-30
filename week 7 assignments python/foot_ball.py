def points():
    num_of_matches = int(input("enter number of matches: "))
    
    points = 0
    if num_of_matches > 0:
        num_wins = int(input("Enter Number Of Wins: "))
        num_loss = int(input("Enter Number Of loss: "))
        num_draws = int(input("Enter Number Of drwas: "))
        if num_wins>0:
            for i in range(num_wins):
                points +=  3
    

        if num_draws>0:
            for i in range(num_draws):
                points += 1
    
        if num_loss>0:
            points +=  0
    else:
        print("please enter correct number of martches")
    
    print(points)


points()