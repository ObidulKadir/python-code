num=int(input("Enter the range:"))
i=1
j=1
for row in range(0,num):
    for col in range(0,num):
        if col==0 or col==num-1:
           print("*",end="")
        elif row == i and col == j:
            print("*", end="")
            i = i + 1
            j = j + 1

        else:
            print(end=" ")

    print()