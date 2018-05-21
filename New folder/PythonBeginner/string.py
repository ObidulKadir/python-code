
'''''name="kadir"
length=len(name)

i=0
for i in range(-1,(-length-1),-1):
    print(name[i],"\t",name[i])
    i+=1'''

#string concatanation

str="welcome to world of ssit01"
substr11="to"
substr2="of"

print (str.index(substr11))
print(str.index(substr11,8))
print (str.index(substr2,6))
print(str.count(substr11))
print(str.isalnum())
print(str.isalpha())
print(str.isdecimal())
print(str.swapcase())