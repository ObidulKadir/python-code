num = int(input("Enter an integer number : "))#maximum for five input
for row in range(0,num):
    for col in range(0,num):
        if col == 0 or col == num-1 :
            print("*", end="")
        elif (row == col and col<3)  or (row == 1 and col == 3):
            print("*", end="")

        else:
            print(end=" ")
    print()