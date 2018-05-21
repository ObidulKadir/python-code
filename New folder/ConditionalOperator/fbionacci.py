
num=int(input("Enter the number:"))

a=0
b=1
c=0

print(a)
print(b)

while (num>0):
    c=a+b
    print(c)

    a=b
    b=c

    num=num-1