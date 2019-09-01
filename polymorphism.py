# polymorphism
# Duck type
# Operating Overloading
# method overloading
# method overriding

# *** duck type
class pycharm():
    def execute(self):
        print("compiling")
        print("running")
class myide():
    def execute(self):
        print("spell check")
        print("convention check")
        print("compiling")
        print("running")

class laptop():
    def code(self,ide):
        ide.execute()

ide = pycharm()
ide1 = myide()
l1=laptop()
l1.code(ide)
l1.code(ide1)
