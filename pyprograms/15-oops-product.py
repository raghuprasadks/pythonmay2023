class Product():
    #Member variables
    code=-1
    name=""
    desc=""
    supplier=""
    price=-1

    def setCode(self,_code):
        self.code =_code

    def getCode(self):
        return self.code

    def setName(self, _name):
        self.name = _name

    def getName(self):
        return self.name

    def info(self):
        return "Code : ",self.code," Name : ",self.name

product1 =Product()
product1.code = 1
product1.name = "Smart phone"
product1.supplier="Apple"
product1.price=100000

info=product1.info()
print("product 1 info",info)

product2 =Product()
product2.setCode(2)
product2.setName("Vivo smart phone")
product2.supplier="Vivo"
product2.price=80000
info=product2.info()
print("product 2 info",info)

# getting the value
print("product 2 suppier ",product2.supplier)


