"""
1. Sum of digits of a given number
for example
sumofdigits(num)
return the sum of digits
123 = 1+ 2+3 = 6
def sumofdigits(num):
    sum=0
    while (num>0) :
       remainder=num%10
       sum=remainder+sum
       num=num//10
    return sum

number=sumofdigits(123)
print(number)
"""
"""
2. Write a function to Reverse a given number
reverse(num)
return the reverse of the number
for example reverse(123)
321
"""
def reverse(num):
    reverse=0
    while (num>0) :
       remainder=num%10
       reverse=reverse*10 +remainder
       num=num//10
    return reverse

n=int(input("Enter a number"))
rev=reverse(n)
print("reverse of number",n , " is ",rev)
print("check whether a given number is palindrome or not")
if (n==rev):
    print(n, " is a palindrome")
else:
    print(n, " is not a palindrome")

