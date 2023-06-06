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
            self.items[item]=float(totalqty)
        else:
            self.items[item]=float(qty)
        return f"Pantry Stock for {item}: {self.items[item]}"

    def get_item(self, item, qty):
        if item in self.items.keys():
            #print("current item ", self.items[item])
            currentqty = self.items[item]
            if (qty>currentqty):
                self.items[item]=0.0
                return f"Add {item} to your shopping list!"
            else:
                #print("curr qty :: ",currentqty)
                totalqty = currentqty-qty
                self.items[item]=totalqty
                return f"You have {self.items[item]} of {item} left"
        else:
            return f"You donot have  {item} "

    def transfer(self,other_pantry, item:str):
        if item in other_pantry.items.keys():
            if item in self.items.keys():
                qty = other_pantry.items[item]
                currentqty=self.items[item]
                totalqty = currentqty + qty
                self.items[item] = totalqty
            else:
                self.items[item] = other_pantry.items[item]
            #del other_pantry.items[item]

sara_pantry = Pantry()
print(sara_pantry.stock_pantry('Bread', 2))
#'Pantry Stock for Bread: 2.0'
# passed

print(sara_pantry.stock_pantry('Cookies', 6))
#'Pantry Stock for Cookies: 6.0'
#passed
print(sara_pantry.stock_pantry('Chocolate', 4))
#'Pantry Stock for Chocolate: 4.0'
#passed
print(sara_pantry.stock_pantry('Pasta', 3))
#'Pantry Stock for Pasta: 3.0'
#passed
print(sara_pantry)
#I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
print(sara_pantry.get_item('Pasta', 2))
#'You have 1.0 of Pasta left'
print(sara_pantry.get_item('Pasta', 6))
#'Add Pasta to your shopping list!'
print(sara_pantry)
#I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
ben_pantry = Pantry()
print(ben_pantry.stock_pantry('Cereal', 2))
#'Pantry Stock for Cereal: 2.0'
print(ben_pantry.stock_pantry('Noodles', 5))
#'Pantry Stock for Noodles: 5.0'
print(ben_pantry.stock_pantry('Cookies', 9))
#'Pantry Stock for Cookies: 9.0'
print(ben_pantry.stock_pantry('Cookies', 8))
#'Pantry Stock for Cookies: 17.0'
print(ben_pantry.get_item('Pasta', 2))
#"You don't have Pasta"

print(ben_pantry.get_item('Cookies', 2.5))
#'You have 14.5 of Cookies left'
print(sara_pantry)
sara_pantry.transfer(ben_pantry, 'Cookies')
print(sara_pantry)
#I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
ben_pantry.transfer(sara_pantry, 'Rice')
ben_pantry.transfer(sara_pantry, 'Pasta')
print(ben_pantry)
#I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
ben_pantry.transfer(sara_pantry, 'Pasta')
print(ben_pantry)
#I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
print(sara_pantry)
#I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}


