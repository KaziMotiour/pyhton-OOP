# class Dog():
#     def __init__(self,bread,name):
#         self.bread = bread
#         self.name  =name
#
# Mydog = Dog("lab","sammi")
# #otherDog = Dog(bread="haski")
# print(Mydog.bread,Mydog.name)
# #print(otherDog.bread)
# # print(type(dog()))

class circle():
    pi=3.14
    def __init__(self,redius=1):
            self.redius=redius

    def area(self):
        return self.redius*self.redius*circle.pi

    def set_redius(self,new_r):
        self.redius = new_r

myc=circle(3)
print(myc.area())
myc.redius=5
print(myc.area())
myc.set_redius(50)
print(myc.area())
print("hello")
print(myc.area())