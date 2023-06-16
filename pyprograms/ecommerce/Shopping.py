import ProductCatalog
import Product
import Customer
import Cart

pcatalog = ProductCatalog.ProductCatalog()
prod1 = Product.Product(1,"Nokia G20 Smartphone",'Dual SIM 4G, 4GB RAM/64GB Storage, 48MP Quad Camera with 6.5” (16.51 cm) Screen | Silver, 4GB+64Gb',"Nokia",9999,10)
pcatalog.addProduct(prod1)
pcatalog.listProduct()
prod1.price=11000
print("product updation")
pcatalog.updateProduct(prod1)
print("after updation")
pcatalog.listProduct()

prod2 = Product.Product(2,"Nokia G10 Smartphone",'Dual SIM 4G, 4GB RAM/64GB Storage, 48MP Quad Camera with 6.5” (16.51 cm) Screen | Silver, 4GB+64Gb',"Nokia",19999,10)
pcatalog.addProduct(prod2)
pcatalog.listProduct()
pcatalog.searchByProductName("nokia G10 ")

cust1 = Customer.Customer(1,"raghu","raghu@gmail.com",9845547471,"jakkuru","Bengaluru")

mycart = Cart.Cart(cust1)
mycart.addCart(prod1)
mycart.addCart(prod2)
mycart.listCart()



