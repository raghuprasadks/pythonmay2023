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
"""

octal = 512
print("The decimal value of",octal, " is",to_decimal(octal))


def to_decimal(oct_num):
    sum=0
    i=0
    base=8
    while (oct_num>0) :
       reminder=oct_num%10
       sum=sum+reminder*base**i
       oct_num=oct_num//10
       i=i+1
    return sum

number=to_decimal(111)
print("Decimal number is :",number)


#list_of_numbers=[]
dict_of_numbers={}
def has_hoagie(num):
    temp_key=0
    while(num>0):
        rem=num%10
        print(rem)
        num=num//10
#        list_of_numbers.append(rem)
        dict_of_numbers[temp_key]=rem
        temp_key+=1
    if (len(dict_of_numbers)>2):
        '''
        prev_element=0
        for i in range(1,len(list_of_numbers)-1):
            next_element=i+1
            if list_of_numbers[prev_element] == list_of_numbers[next_element] :
                print("It has hoagie")
            prev_element=prev_element+1
        '''
        prev_element=0
        for i in range(1,len(dict_of_numbers)-1):
            next_element=i+1
            if dict_of_numbers[prev_element] == dict_of_numbers[next_element] :
                print("It has hoagie")
            prev_element=prev_element+1
has_hoagie(1235)

has_hoagie(737)
