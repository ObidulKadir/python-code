

#Define a class.

class Resturant:

    name = "shayan "
    owner = "kadir "
    address = "sjfnf"

    def details(self):
        print(self.name,self.owner)


    def owner_details(self,address ="sfn"):
        print(self.name,self.owner)
        print(address)


Resturant1 = Resturant();
Resturant1.name = "shayfan"
#Resturant1.owner = "Kadir"

Resturant1.owner_details()
print(type(Resturant1))