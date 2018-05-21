
class Math:

    #s =0
    def __init__(self, x, y):
         self.x = x
         self.y = y


    def sum(self):
        return self.x + self.y

class mathextend1 (Math):
    def __init__(self, x, y):
         self.x = x
         self.y = y


    def sub(self):
        return self.x - self.y
    def sum(self):
        return self.x + self.y + 100   #method overriding

    def show_all(self):
        print("sum: "+ str(super().sum()))
        print("Sum: "+ str(self.sum()))

        print("sub: "+ str(self.sub()))

math_obj = mathextend1(10,12)

math_obj.show_all()