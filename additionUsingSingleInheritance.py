class addition:
    def add1(self):
        print(self.a+self.b)
class values(addition):
    def getvalues(self):
        self.a=int(input("enter the value of a : "))
        self.b=int(input("Ente the value of b : "))

c=values()
c.getvalues()
c.add1()