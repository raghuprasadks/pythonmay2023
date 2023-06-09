"""
def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)


#fact = factorial(3)
#print(fact)


# Program to print the fibonacci series upto n_terms

# Recursive function
def recursive_fibonacci(n):
    if n <= 1:
	    return n
    else:
	    return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

n_terms = 5

# check if the number of terms is valid
if n_terms <= 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
    for i in range(n_terms):
	    print(recursive_fibonacci(i))
"""
"""
term = 5

fibonacci series 0 1 1 2 3
"""
"""
https://www.geeksforgeeks.org/count-the-occurence-of-digit-k-in-a-given-number-n-using-recursion/
"""
def consecutive_digits (num):
    isConsecutive=False
    numdict={}
    prev_digit=-1
    while(num>0):
        current_digit=num%10
        if(prev_digit==current_digit):
            #print("consecutive digit ",current_digit)
            isConsecutive=True
            return isConsecutive
            #break
        num = num//10
        prev_digit=current_digit
    return isConsecutive

print(consecutive_digits(2222466666678))
print(consecutive_digits(123456))


def only_evens(num):
    evennums:int=0
    while(num>0):
        leastsignificant = num%10
        if(leastsignificant%2==0):
            evennums=evennums*10+leastsignificant
            #print(leastsignificant,end='')
        num=num//10
    return evennums


def reversenum(num):
    reversednum=0
    while (num>0):
        remainder = num%10
        reversednum=reversednum*10+remainder
        num = num//10
    return reversednum
result = only_evens(4386112)
print("even",result)
reversedn=reversenum(result)
print("final",reversedn)

def only_evens_recursion(num):
        if (num<0):
            return 0
        leastsignificant = num%10
        if(leastsignificant%2==0):
            return leastsignificant*10+only_evens_recursion(num=num//10)



def consecutive_digits_recursion (num):
    if(num==0):
        return
    current_digit=num%10
    remaining_digit = num//10
    return consecutive_digits_recursion(remaining_digit)
    #min = a if a < b else b
    isConsecutive = True if (previous_digit:int== current_digit) else False
    return isConsecutive
    previous_digit=current_digit



print(consecutive_digits_recursion(2222466666678))
print(consecutive_digits_recursion(123456))
