
num=int(input("Enter the range :"))
i = 3
j = 1
x = 0
z = 2
for row in range(0,num):
    for col in range(0,num - 2):

        if col == 0:
            print("*",end="")
        elif row == i and col == j:
            print("*",  end="")
            i = i + 1
            j = j + 1
        elif row == x and col == z:
            print("*", end="")
            x = x + 1
            z = z - 1
        else:
            print(end=" ")

    print()
