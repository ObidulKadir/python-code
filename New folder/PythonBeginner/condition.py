
#conditional Satement
'''''
n =not (4<5 or 7>2)

print(n)


#membership Operator

list=[10,20,"shayan",24]

a=10
b="kadir"
if a in list :
    print ("a in list")

else:
    print ("not in list")

if (b not in list):
    print ("b not in list")

else:
    print("b in list")
    '''

#Identity Operator

a=10
b=12

if (a is b): #matching two operand
    print("two operand same are same identity")

elif (a is not b):
    print ("two operand is not same identity")
else:
    print("default")