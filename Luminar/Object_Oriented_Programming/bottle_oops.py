class Bottle:
    material:str
    capacity:str
    price:int
    color:str

    def __init__(self,**kwargs):
        self.material=kwargs.get("material")
        self.capacity=kwargs.get("capacity")
        self.price=kwargs.get("price")
        self.color=kwargs.get("color")
    def open(self):
        print("open")

    def print_details(self):
        print(self.price,self.material)

bt=Bottle(material="plastic",capacity="800ml",price="150",color="transparent")

bt.print_details()



# constructor - initializing instance variable

# constructor name is always __init__  in python