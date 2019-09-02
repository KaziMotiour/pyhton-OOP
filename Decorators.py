# s = "Global variable"
#
# def func():
#     # global s
#     # s = 10
#     # print(s)
#     my_locla = 40
#     print(locals())  # return a dictionary
#
# func()

# show all the uppercase in text
# def hello(name):
#         print("this is a sunny day")
#
#         def greet():
#             return "I'm in greet function"
#
#         def welcome():
#             return "welcome to my function"
#         if name == 'motiour':
#             return greet()
#         else:
#             return welcome()
# print(hello(input()))

# Decorates
# def hello():
#     print("hello matiour")
# def other(func):
#     print("Hello tareek")
#     return func
# other(hello())
def new_decorator(func):

    def call_func():
        print("Code here before execution func")
        func()
        print("Func() has been called")
    return call_func
@new_decorator
def Func_need_decorator():
    print("This function is in need of a Decorator")
#Func_need_decorator = new_decorator(Func_need_decorator())
Func_need_decorator()