class student:
    def __init__(self,m1,m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
            m1 = self.m1 + other.m1
            m2 = self.m2 + other.m2
            s3 = student(m1, m2)
            return s3
    def __mul__(self, other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        s4 = student(m1,m2)
        return s4

s1 = student(58,68)
s2 = student(60,65)
s3 = s1 + s2
s4 = s1 * s2
# print(s3[0])
# print(s3[1])
print(s4.m1)
print(s4.m2)


# class book():
#     def __init__(self,price,price1):
#         self.price = price
#         self.price1 = price1
#     def __add__(self, other):
#         a = self.price + other.price
#         b = self.price1 + other.price1
#         return a,b
#
#
#
# book1 = book(10,20)
# book2 = book(20,20)
# total_price = book1 + book2
# print(total_price)