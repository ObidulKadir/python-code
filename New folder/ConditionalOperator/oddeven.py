
num=input("Enter the positive vaues:")
a=int(num)

if (a>=80 and a<=100):
    print("Your Grade is \t A+")

elif (a>=75 and a<=80):
    print("Your Grade is \t A")

elif (a>=70  and a<=75):
    print("Your grade is \t A-")

elif (a>=65 and a<=70):
    print("Your grade is \t B+")

elif (a>=60and a<=65):
    print("Your grade is \t B")

elif (a >= 55 and a <= 60):
    print("Your grade is \t B-")

elif (a>=50 and a<=55):
    print("Your grade is \t C+")

elif (a>=45 and a<=50):
    print("Your grade is \t C")

elif (a>=40 and a<=45):
    print("Your grade is \t D")

elif (a>=0 and a<=39):
    print("You are FAIL.")
else:
    print("you entered wrong values")