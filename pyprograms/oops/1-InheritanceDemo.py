class Vehicle():

    def __init__(self,number,owner,make,model,price,color):
        self.number = number
        self.owner = owner
        self.make = make
        self.model = model
        self.price  = price
        self.color = color
        self.speed = None


    def start(self):
        self.speed = 0
        print("Vehicle :start")

    def move(self):
        self.speed = self.speed +10
        print("Vehicle :move",self.speed)

    def stop(self):
        self.speed = 0
        print("Vehicle :stop")


    def __str__(self):
        return f'Number : {self.number} Owner: {self.owner} make : {self.make} '


veh1 = Vehicle('KA 05 MN 6677','raghu','huyndai','Aastha',700000,'brown')
print(veh1)

class Bike(Vehicle):
    def __init__(self,number,owner,make,model,price,color):
        super().__init__(number,owner,make,model,price,color)

bike1 = Bike('KA 05 MN 9999','raghu','honda','super move',200000,'black')
print(veh1)
bike1.start()
bike1.move()
bike1.stop()



