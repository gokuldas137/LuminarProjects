class Mysampleclass():
    def hello(self,n):
        self.name=n
        print(self.name)

x=Mysampleclass()
y=Mysampleclass()

name="Gokul Das"

x.hello(name)

y.hello("Das")