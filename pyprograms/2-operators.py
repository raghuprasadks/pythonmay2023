"""
Operators -
Arithmetic - +,-,*,/,//,%
Comparision operator - >,>=,<,<=,==,!=
Logical operators - and or not
"""

print("Arithmetic Operators")

num1=100
num2=200
result = num1+num2
print("Result of addition of ",num1," and ",num2," is ",result)

num3=9
num4=2
result =num3/num4
print(num3," / ",num4," = ",result)
result =num3//num4
print(num3," // ",num4," = ",result)

result =num3%num4
print(num3," % ",num4," = ",result)
print("Comparision")
result = num1>num2
print(" num1>num2 ",result)

result = num1==num2
print(" num1==num2 ",result)

result = num1!=num2
print(" num1!=num2 ",result)
print(100>=100)
print("logical operators")
result = (num2>num1) and (num3>num4)
print("result of and ",result)

result = (num2==num1) or (num3>num4)
print("result of or ",result)

result = not ((num2==num1) or (num3>num4))
print("result of not ",result)