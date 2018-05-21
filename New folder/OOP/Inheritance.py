

class Math:

    #s =0
    def __init__(self, x, y):
         self.x = x
         self.y = y


    def sum(self):
        return self.x + self.y



class Mathextended1 (Math):

    def __init__(self, x, y):
        super().__init__(x, y)

    def subtraction(self):
        return  self.x - self.y

#Multiple Inheritance

class Mathextra:

    def division(self, x, y):
        return x/y


class Mathextended2(Mathextended1,Mathextra):

    def __init__(self , x, y):
        super().__init__(x,y)



    def multiplication(self, x, y ):
        return self.x * self.y

math_obj = Mathextended2(2, 5)
print("Summation =",str(math_obj.sum()))
print("Subtraction =",str(math_obj.subtraction()))
print("Multiplication = ",str(math_obj.multiplication(x=math_obj.x,y=math_obj.y)))
print("Division = ",str(math_obj.division(x=math_obj.x,y=math_obj.y)))