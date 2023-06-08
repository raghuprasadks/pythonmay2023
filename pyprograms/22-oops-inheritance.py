class Vehicle:
    """
    Properties/attributes
    """
    manufacturer:str
    model:str
    regno:str
    owner:str
    color:str
    price:int
    speed:int
    """
    Constructure
    """
    def __init__(self,manu,model,regno,owner,color,price):
        self.manufacturer=manu
        self.model=model
        self.regno = regno
        self.owner = owner
        self.color= color
        self.price = price
    def start(self):

        self.speed = 0
        print("Vehicle : started")

    def move(self):
        self.speed = self.speed+10
        print("Vehicle: moved :speed ",self.speed)

    def stop(self):
        self.speed = 0
        print("Vehicle : stopped")

    def info(self):
        return f"Manufacturer {self.manufacturer} Model : {self.model}"

#veh1 = Vehicle()
veh1 = Vehicle("Maruti","Swift","KA05 MN6677","Ravi","Red",650000)
veh1.manufacturer="Maruti"
veh1.model="Swift"
veh1.owner="Suresh"

info = veh1.info()
print(info)
#veh1.test()

"""
Constructure - special method to create object by 
passing the required property
"""

class Bike(Vehicle):
    def test(self):
        print("test drive")

    """
    method overriding
    """
    def move(self):
        self.speed = self.speed+20
        print("Bike: moved :speed ",self.speed)

    def stop(self):
        print("calling stop of base")
        Vehicle.stop(self)



mybike = Bike("Yamaha","Super 100","KA05 MN6666","Ravi","Black",250000)
mybike.start()
mybike.move()
mybike.move()
mybike.stop()
#print("base : " ,mybike.Vehicle.move())

info =mybike.info()
print("Info about my bike ",info)
mybike.test()