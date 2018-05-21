
#Object LifeCycle

class X:
    def __init__ (self,name):
        self.name = name
        print(self.name + " is created.")


    def __del__(self):
        print(self.name + " is distroyed.")

        #uncomment this to check to life cyle


x = X("X")
y = X("Y")

print("Hello world!!!!")

def hello():
    x = X("Hello")
    y = X("hello")

hello()



