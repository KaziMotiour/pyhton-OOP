class school():
    def __init__(self):
        self.name='BN collage'
        self.address='Mirpu-14'
    def show(self):
        print('Name of collage: '+self.name+'\nAddress: '+self.address)


class student():

    def __init__(self,name,id):
        self.name=name
        self.id=id
        self.lap=self.laptop()  # call the inner class
        self.collage=school()  # call the outer class
    def student_info(self):
        print('Name of student: '+ self.name+'\nId: '+str(self.id))

    class laptop():  # inner class
        def __init__(self):
            self.name='dcl'
            self.model='i3'
            self.ram='8gb'
        def show(self):
            print('Laptop name: '+self.name+'\nLaptop model: ' +self.model+'\nRam: '+self.ram)

s1=student('Matiour','171-15-8649')
s1.collage.show()
s1.student_info()
s1.lap.show()