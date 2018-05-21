
def person_bio(name,age,country="US"):#non-default argument follows default argument
    print(name,age,country,sep="-")

person_bio("kadir",'bangladesh',23)
person_bio(name="kadir",age=23,country="desh")
person_bio("shayan",24)