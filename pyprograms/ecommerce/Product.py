class Product():
    """
    properties
    """
    code:int=0
    #code=0
    name:str
    desc:str
    supplier:str
    price:int
    stock:int=0
    """
    constructor in python
    """
    def __init__(self,code,name,desc,supplier,price,stock=5):
        self.code = code
        self.name = name
        self.desc = desc
        self.supplier = supplier
        self.price = price
        self.stock =stock

    def information(self):
        return f"\n Code:{self.code} \n Name: {self.name} \n Desc: {self.desc} \n Supplier: {self.supplier} \n Price: {self.price} \n Stock: {self.stock}"


    def __str__(self):
        return f"\n Code:{self.code} \n Name: {self.name} \n Desc: {self.desc} \n Supplier: {self.supplier} \n Price: {self.price} \n Stock: {self.stock}"

    def __repr__(self):
        return f"Product({self.code},{self.name},{self.desc},{self.supplier},{self.price},{self.stock})"


"""
prod1 = Product()
prod1.code=1
prod1.name="Nokia G20 Smartphone"
prod1.desc='Dual SIM 4G, 4GB RAM/64GB Storage, 48MP Quad Camera with 6.5” (16.51 cm) Screen | Silver, 4GB+64Gb'
prod1.supplier="Nokia"
prod1.price=9999
print(prod1.information())

prod2 = Product()
prod2.code=2
prod2.name="Nokia G20 Smartphone"
prod2.desc='Dual SIM 4G, 4GB RAM/64GB Storage, 48MP Quad Camera with 6.5” (16.51 cm) Screen | Silver, 4GB+64Gb'
prod2.supplier="Nokia"
prod2.price=9999
"""
prod1 = Product(1,"Nokia G20 Smartphone",'Dual SIM 4G, 4GB RAM/64GB Storage, 48MP Quad Camera with 6.5” (16.51 cm) Screen | Silver, 4GB+64Gb',"Nokia",9999,10)
print("prod1:str")
print(str(prod1))
print("prod1:repr")
print(repr(prod1))



#info = prod1.information()
#print("product 1")
#print(info)

prod2 = Product(2,"Nokia G20 Smartphone new",'Dual SIM 4G, 4GB RAM/64GB Storage, 48MP Quad Camera with 6.5” (16.51 cm) Screen | Silver, 4GB+64Gb',"Nokia",12999)
info = prod2.information()
print("product 2")
print(info)