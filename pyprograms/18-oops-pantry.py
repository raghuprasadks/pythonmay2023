class Pantry():
    #items: dict={}

    def __init__(self):
        self.items ={}

    def __repr__(self):
        return f"I am a Pantry object, my current stock is {self.items}"

    def stock_pantry(self,item:str,qty:float):
        #print("keys ",self.items.keys())
        if item in self.items.keys():
            #print("current item ", self.items[item])
            currentqty = self.items[item]
            #print("curr qty :: ",currentqty)
            totalqty = currentqty+qty
            self.items[item]=totalqty
        else:
            self.items[item]=qty

    def get_item(self, item, qty):
        if item in self.items.keys():
            #print("current item ", self.items[item])
            currentqty = self.items[item]
            if (qty>currentqty):
                print(f"Add {item} to your shopping list!")
            else:
                #print("curr qty :: ",currentqty)
                totalqty = currentqty-qty
                self.items[item]=totalqty
                print(f"You have {self.items[item]} of {item} left")
        else:
            print (f"You donot have  {item} ")

    def tranfer(self,other_pantry, item:str):
        if item in self.items.keys():
            qty = other_pantry.items[item]
            currentqty=self.items[item]
            totalqty = currentqty + qty
            self.items[item] = totalqty
        else:
            self.items[item] = other_pantry.items[item]
        del other_pantry.items[item]

sara_pantry = Pantry()
print(sara_pantry)
sara_pantry.stock_pantry('Bread', 2)
print("After adding bread")
print(sara_pantry)

sara_pantry.stock_pantry('Lettuce', 1.5)
print("After adding Lettuce")
print(sara_pantry)

sara_pantry.stock_pantry('Lettuce', 2)
print("After adding Lettuce one more time")
print(sara_pantry)
sara_pantry.get_item('Lettuce', .5)

sara_pantry.get_item('dal', .5)

ben_pantry = Pantry()
print("Ben pantry """,ben_pantry)
ben_pantry.stock_pantry("Cereal",2)
ben_pantry.stock_pantry("Noodles",5)
print("ben pantry",ben_pantry)
sara_pantry.tranfer(ben_pantry,"Noodles")
print("sara pantry",sara_pantry)
print("after tranfer :ben pantry",ben_pantry)

