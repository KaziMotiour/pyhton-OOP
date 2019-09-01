# enclosing function locals
name = "Hello this is motiour"
def my_name():
    name = "Hello matiour!"
    def hello():
        print(name)
    hello()
my_name()
print(name)

# use global to change local variable

x = 50
def func():
    global x
    x=100
print(x)
func()
print(x)