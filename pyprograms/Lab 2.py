# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import random
import math

# -------- SECTION 1
"""
class Instructor:
    '''
        >>> t1= Instructor('John Doe')
        >>> t1.get_name()
        'John Doe'
        >>> t1.get_courses()
        []
        >>> t1.add_course('MATH140')
        >>> t1.get_courses()
        ['MATH140']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH141')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH140')
        >>> t1.get_courses()
        ['STAT100']
    '''

    def __init__(self, name):
    #--- YOUR CODE STARTS HERE
        self.name = name
        self.courses = []

    def get_name(self):
    #--- YOUR CODE STARTS HERE
        return self.name

    def set_name(self, new_name):
    #--- YOUR CODE STARTS HERE
        self.name = new_name

    def get_courses(self): #function to get the courses taught by the instructor
    #--- YOUR CODE STARTS HERE
        return self.courses

    def remove_course(self, course): #function to remove a course
    #--- YOUR CODE STARTS HERE
        if course in self.courses:
            self.courses.remove(course)

    def add_course(self,course): #function to add a course
    #--- YOUR CODE STARTS HERE
        if course not in self.courses:
            self.courses.append(course)

"""
# -------- SECTION 2      
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """

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
                return f"Add {item} to your shopping list!"
            else:
                #print("curr qty :: ",currentqty)
                totalqty = currentqty-qty
                self.items[item]=totalqty
                return f"You have {self.items[item]} of {item} left"
        else:
            return f"You donot have  {item} "

    def tranfer(self,other_pantry, item:str):
        if item in self.items.keys():
            qty = other_pantry.items[item]
            currentqty=self.items[item]
            totalqty = currentqty + qty
            self.items[item] = totalqty
        else:
            self.items[item] = other_pantry.items[item]
        del other_pantry.items[item]

"""
# -------- SECTION 3
class Vendor:

    def __init__(self, name):
        '''
            In this class, self refers to Vendor objects
            
            name: str
            vendor_id: random int in the range (999, 999999)
        '''
        self.name = name
        self.vendor_id = random.randint(999, 999999)
    
    def install(self):
        '''
            Creates and initializes (instantiate) an instance of VendingMachine 
        '''
        return VendingMachine()
    
    def restock(self, machine, item, amount):
        '''
            machine: VendingMachine
            item: int
            amount : int/float

            Call _restock for the given VendingMachine object
        '''
        return machine._restock(item, amount)
        


class VendingMachine:
    '''
        In this class, self refers to VendingMachine objects

        >>> john_vendor = Vendor('John Doe')
        >>> west_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> john_vendor.restock(west_machine, 215, 9)
        'Invalid item'
        >>> west_machine.isStocked
        True
        >>> john_vendor.restock(west_machine,156, 1)
        'Current item stock: 4'
        >>> west_machine.getStock
        {156: [1.5, 4], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Please deposit $1.5'
        >>> west_machine.purchase(156,2)
        'Please deposit $3.0'
        >>> west_machine.purchase(156,23)
        'Current 156 stock: 4, try again'
        >>> west_machine.deposit(3)
        'Balance: $3.0'
        >>> west_machine.purchase(156,3)
        'Please deposit $1.5'
        >>> west_machine.purchase(156)
        'Item dispensed, take your $1.5 back'
        >>> west_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> west_machine.deposit(300)
        'Balance: $300.0'
        >>> west_machine.purchase(876)
        'Invalid item'
        >>> west_machine.purchase(384,3)
        'Item dispensed, take your $292.5 back'
        >>> west_machine.purchase(156,10)
        'Current 156 stock: 3, try again'
        >>> west_machine.purchase(156,3)
        'Please deposit $4.5'
        >>> west_machine.deposit(4.5)
        'Balance: $4.5'
        >>> west_machine.purchase(156,3)
        'Item dispensed'
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 3], 384: [2.5, 0], 879: [3.0, 3]}
        >>> west_machine.purchase(156)
        'Item out of stock'
        >>> west_machine.deposit(6)
        'Balance: $6.0'
        >>> west_machine.purchase(254,3)
        'Item dispensed'
        >>> west_machine.deposit(9)
        'Balance: $9.0'
        >>> west_machine.purchase(879,3)
        'Item dispensed'
        >>> west_machine.isStocked
        False
        >>> west_machine.deposit(5)
        'Machine out of stock. Take your $5.0 back'
        >>> west_machine.purchase(156,2)
        'Machine out of stock'
        >>> west_machine.purchase(665,2)
        'Invalid item'
        >>> east_machine = john_vendor.install()
        >>> west_machine.getStock
        {156: [1.5, 0], 254: [2.0, 0], 384: [2.5, 0], 879: [3.0, 0]}
        >>> east_machine.getStock
        {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        >>> east_machine.deposit(10)
        'Balance: $10.0'
        >>> east_machine.cancelTransaction()
        'Take your $10.0 back'
        >>> east_machine.purchase(156)
        'Please deposit $1.5'
        >>> east_machine.cancelTransaction()
    '''

    def __init__(self):
        #--- YOUR CODE STARTS HERE
        self.vending = {156: [1.5, 3], 254: [2.0, 3], 384: [2.5, 3], 879: [3.0, 3]}
        self.balance = 0.0
        self.transitem = None
        self.transqty = 0


    def purchase(self, item, qty=1): # function to buy from vending machine
        #--- YOUR CODE STARTS HERE
        if item not in self.vending:
            return "Invalid item"

        if qty > self.vending[item][1]:
            return f"Current {item} stock: {self.vending[item][1]}, try again"

        price = self.vending[item][0] * qty

        if self.balance < price:
            return f"Please deposit ${price}"

        self.balance -= price
        self.vending[item][1] -= qty

        if self.vending[item][1] == 0:
            self.vending.pop(item)

        return "Item dispensed"


    def deposit(self, amount): # adding money to the vending machine balance
        #--- YOUR CODE STARTS HERE
        if self.isStocked():
            self.balance += amount
            return f"Balance: ${self.balance}"
        else:
            return f"Machine out of stock. Take your ${amount} back"


    def _restock(self, item, stock): # function to restock an item to vending machine
        if item in self.vending:
            self.vending[item][1] += stock
            return f"Current item stock: {self.vending[item][1]}"
        else:
            return "Invalid item"


    def isStocked(self): # function to check if the machine has any items in stock
        return bool(self.vending)


    def getStock(self): # function to get current stock 
        return self.vending.copy()


    def cancelTransaction(self): # function to cancel the transaction    
        #--- YOUR CODE STARTS HERE
        if self.transitem is not None:
            refund = self.vending[self.transitem][0] * self.transqty
            self.balance -= refund
            self.transitem = None
            self.transqty = 0
            return f"Take your ${refund} back"
        else:
            return None


# -------- SECTION 4
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line1==line2
        False
        >>> line3==line2
        True
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line5==9
        False
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''
    def __init__(self, point1, point2):
        #--- YOUR CODE STARTS HERE
        self.point1 = point1
        self.point2 = point2

    #--- YOUR CODE STARTS HERE
    def getDistance(self): #function to find distance between two points
        return round(math.sqrt((self.point2.x - self.point1.x)**2 + (self.point2.y - self.point1.y)**2),3)
       
    
    #--- YOUR CODE STARTS HERE
    def getSlope(self): #function to find slope between two points
        return round((self.point2.y - self.point1.y)/(self.point2.x - self.point1.x),3)


    #--- YOUR CODE CONTINUES HERE
    def __str__(self): #string representation of line equation
        slope = self.getSlope()
        if slope == float('inf'):
            return "Undefined"
        elif slope == 0:
            return f"y = {self.point1.y}"
        else:
            return f"y = {slope}x + {self.point1.y - slope*self.point1.x}"

    
    def __eq__(self, other): #function to check if two lines are equal
        if isinstance(other, Line):
            return self.getSlope() == other.getSlope() and self.point1.y == other.point1.y
        return False

    def __mul__(self, factor): #function fo support the * operator
        newpoint1 = Point2D(self.point1.x * factor, self.point1.y * factor)
        newpoint2 = Point2D(self.point2.x * factor, self.point2.y * factor)
        return Line(newpoint1, newpoint2)

    def __contains__(self, point): #function to check if a point lies on the line
        if isinstance(point, Point2D):
            return (point.y - self.point1.y) == self.getSlope() * (point.x - self.point1.x)
        return False
"""
def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=True)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace intersection with the name of the function you want to test
    #doctest.run_docstring_examples(Pantry, globals(), name='LAB2',verbose=True)

if __name__ == "__main__":
    run_tests()
