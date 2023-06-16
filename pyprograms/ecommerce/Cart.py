class Cart():
    def __init__(self,customer):
        self.mycart=[]

    def addCart(self,product):
        self.mycart.append(product)

    def listCart(self):
        for prod in self.mycart:
            print(prod)
