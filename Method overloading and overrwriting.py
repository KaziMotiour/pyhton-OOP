# method overloading
class sturdent():
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c
        elif a!=None and b!=None:
            return a+b
        else:
            return a
s1 = sturdent(50, 69)
print(s1.sum(5))

# method overriding

class a:
    def show(self):
        print("show in a")

class b(a):
    def show(self):
        print("show in b")

b1 = b()
b1.show()