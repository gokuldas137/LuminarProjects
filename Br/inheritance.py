class BaseClass:
    def set_name(self,name):
        self.name=name



class SubClass(BaseClass):
    def welcome(self):
        print("Welcome")

    def display(self):
        print("Name: "+self.name)



y=SubClass()

y.welcome()
y.set_name("Gokul")
y.display()