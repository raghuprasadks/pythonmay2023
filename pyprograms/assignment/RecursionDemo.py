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
    numdict={}
    while(num>0):
        digit=num%10
        if digit in numdict.keys():
            currentcount = numdict[digit]
            numdict[digit]=currentcount+1
        else:
            count = 1
            numdict[digit] = count

        num = num//10
    print(numdict)

consecutive_digits(2222466666678)


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


