
#3 object created

class Person:

    def __init__(self,name,age):
        self.name=name
        self.age = age

    def change_name(self,name):
        self.name = name
    def details(self):
        print(self.name, self.age , sep=' | ')
'''''
bill = Person('kadir',24)
bill.details()
print(bill.name,bill.age)'''

'''''people_list = []

for i in range(0,3):
    person = Person("Person "+str(i),23+i)
    people_list+=[person]

for i in people_list:
    i.details()'''

person_x = Person(name="Obidul kadir",age="25")
person_x.details()

person_x.change_name("rizwan")
person_x.details()