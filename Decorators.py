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

def hello(name):
        print("this is a sunny day")

        def greet():
            return "I'm in greet function"

        def welcome():
            return "welcome to my function"
        if name == 'motiour':
            return greet()
        else:
            return welcome()
print(hello(input()))