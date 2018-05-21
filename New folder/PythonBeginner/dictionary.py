
'''''
dict={tap:value}
'''
dict = {}
print(type(dict))
dict['name']="kadir"
dict['age']=23
dict[1]=88
print(dict['name'] ," |",dict['age']," ",dict[1])

dict={"bill":"028492u4","kul":"947862384"}

print(dict['bill'])
print(len(dict))
dict={1: 'Ravi', 2: 'Manoj', 4: 'Om', 5: 'Hari'}

for key ,value in dict.items():
    print(key,value,sep="->")

shop_item={'rice' : 45,
           'flour' : 33,
           'oil' :34}

print(shop_item)
for key in sorted(shop_item.keys()):
    print(key,shop_item[key])

shop_item.clear()
print(shop_item)
