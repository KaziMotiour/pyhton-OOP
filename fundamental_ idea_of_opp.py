# class Dog():
#     def __init__(self,bread,name):
#         self.bread = bread
#         self.name  = name
#
# Mydog = Dog("lab","sammi")
# #otherDog = Dog(bread="haski")
# print(Mydog.bread,Mydog.name)
# #print(otherDog.bread)
# # print(type(dog()))

class circle():
    pi = 3.14
    def __init__(self,radius=1):
            self.radius = radius

    def area(self):
        return self.radius*self.radius*circle.pi

    def set_radius(self,new_r):
        self.radius = new_r

myc=circle(3)
print(myc.area())
myc.radius=5
print(myc.area())
myc.set_radius(50)
print(myc.area())
print("hello")
print(myc.area())