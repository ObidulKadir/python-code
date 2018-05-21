
def sum(x,y):
    return x + y

def sub(x,y):
    return x - y

class Math:

    def __init__(self, x, y):
        self.x = x     #  _x is private
        self.y = y

    def sum(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def div(self):
        return self.x / self.y
'''math =Math(2,5);
print(math.sum())

#Program will shown wrong because _x and _y is a private property.
'''
