"""
print("Handling of zero division exception")
n1 = int(input("Enter first number"))
n2 = int(input("Enter second number"))
result = 0
try:
    result = n1/n2
except:
    print("zero division error")
print("result of division ",result)
"""
"""
print("handling of another error")
n1 = int(input("Enter first number"))
n2 = input("Enter second number")
result = 0
try:
    result = n1/n2
except Exception as ex:
    print("Error ",ex)
print("result of division ",result)
"""

print("Handling of multiple exceptions")
n1 = int(input("Enter first number"))
result = 0
try:
    n2 = int(input("Enter second number"))
    result = n1/n2
except ZeroDivisionError as ex:
    print("ZeroDivisionError")
    print(ex)
except TypeError as ex:
    print("TypeError")
    print(ex)
except Exception as ex:
    print("Any other error")
    print(ex)
finally:
    print("finally :is executed every time")
print("result of division ",result)
