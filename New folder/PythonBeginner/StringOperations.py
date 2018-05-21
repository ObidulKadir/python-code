'''''
a=" i am kadir"
b="cccc"
name = a+b
print(name.isspace())
print (name.title())
print (name.upper())
print(name.lower())
print (name.title().upper())
#white space

name = "    MR.x    "

print (name)

print("_"+name +"_")
print("_"+name.lstrip() + "_")
print("_"+name.rstrip()+ "_")
print("_"+name.lstrip().rstrip()+"_")
print("_"+name.strip()+"_")'''
#single qoute and double quote
name="kadir.and i am engineer"
print(name.find("i"))
print(name.find("fsf"))

print(name.replace('kadir','shayan'))

#string interpolation

name = "{name}'s age is a {age}"

print(name.format(name='kadir',age=23))

name = "taylor"
name1="swift"
#print(name[7:-1])
print(name,name1,sep=("|"))















