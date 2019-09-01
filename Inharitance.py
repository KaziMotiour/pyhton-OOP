class A():
    def freautreA1(self):
        print("Feature A1 is working")
    def freautreA2(self):
        print("Feature A2 is working")
class B():
    def __init__(self):
        self.c = self.c()
    def freautreB1(self):
        print("Feature B1 is working")
    def freautreB2(self):
        print("Feature B2 is working")
    class c():
        def __init__(self):
            #self.m = self.m()
            print("Class c is on")
            self.sk="sk"
        def model(self):
            print("Model : 2018")
        class m():
            def __init__(self):
                print("none")
            def none(self):
                print("text")
B.c.m().none()