
num=int(input("Enter the number:"))
rev=0
count=0
while(num>=1):
    tem = num % 10
    rev = rev * 10 + tem
    num =num//10
    count = count + 1

print(rev)
print(count)

