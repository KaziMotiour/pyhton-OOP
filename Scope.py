# enclosing function locals
name = "Hello this is motiour"
def my_name():
    name = "Hello matiour!"
    def hello():
        print(name)
    hello()
my_name()
print(name)
