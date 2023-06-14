import Product

class ProductCatalog():

    def __init__(self):
        self.productlist=[]

    def addProduct(self,product):
        print("add")
        self.productlist.append(product)

    def listProduct(self):
        print("list")
        for p in self.productlist:
            print(p)

    def updateProduct(self,product):
        for p in self.productlist:
            if(p.code==product.code):
                p=product


