class pycharm():
    def execute(self):
       print("dcl")

class netbins():
    def execute(self):
        print("versio 2.0")

class dev():
    def execute(self,ide):
        ide.execute()
ide1=pycharm()
dev1=dev()
dev().execute(ide1)
