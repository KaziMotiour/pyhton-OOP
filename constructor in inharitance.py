class A():
    def __init__(self):
        print("I'm in A")
    def featuresA(self):
        print("sorry no feature available in A")
class B():
    def __init__(self):
        #super().__init__()
        print("I'm in B")
    def featuresb(self):
        print("sorry no feature available in B")
# class C(B):
#     def __init__(self):
#         super().__init__()
#         print("I'm in C")
#     def featuresb(self):
#         print("sorry no feature available in C")

class C(A,B):
    def __init__(self):
        super().__init__()
        print("I'm in C")
    def featuresC(self):
        print("sorry no feature available in C")


C1 = C()