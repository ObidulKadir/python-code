
list=[1,2,3,4,5]
dict= {"one":1,"two":2,"three":3}

def change_num(list,dict):
    del list[0]
    list[-1]=100

    del dict['one']
    dict['three']=33

    print("Inner list: ",list)
    print("inner dictionary: ",dict)


print("before")
print("oUTER LIST:",list)
print("Outer list: ",dict)

change_num(list=list,dict=dict)

print("After:    ")

print("After List:",list)
print("After Dict..",dict)