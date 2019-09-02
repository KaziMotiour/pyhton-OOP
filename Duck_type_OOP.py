from duck_type import *

def ex(ide):
    ide.execute()
a=input("enter the neme of ide:")

if a=="pycharm":
    ide1=pycharm()
    ex(ide1)
elif  a =="netbins":
    ide2=netbins()
    ex(ide2)
elif a == "dev":
    ide3=dev()
    ex(ide3)
else:
    print("Sorry! this ide is not available right now")


