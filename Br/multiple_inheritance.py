class first():
    def display_first(self):
        print("first")

class second(first):
    def display_second(self):
        print("second")


class third(second):
    def displaythird(self):
        print("Third")

x=third()
x.displaythird()
x.display_second()
x.display_first()