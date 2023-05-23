"""
function
"""
def greet():
    print("Welcome to python")

greet()
greet()

def add(n1,n2):
    print("sum = ",n1+n2)

add(100,200)
add(400,300)

def multiply(num1,num2):
    return num1*num2

result = multiply(20,10)
print("multiplication = ",result)

def isOddOrEven(num):
    if num%2==0:
        print(num, " is even")
    else:
        print(num, " is odd")

isOddOrEven(8)
isOddOrEven(9)