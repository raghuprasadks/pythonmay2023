def factorial(n):
    if(n==1):
        return 1
    else:
        return n*factorial(n-1)
print("Factorial")
print(factorial(3))
"""
3X2X1
1
3*fact(3-1) 
3*fact(2) - 3*2*1
fact(2) = 2*fact(1)=2X1
fact(1)=1

3*2*1*fact(1)
3*fact(2)-3*2*1
2*fact(1) - 2 *1
fact(1)-1
"""


def only_evens(num):
    if num == 0 or None:
        return 0
    cur_dig = num % 10
    if cur_dig%2==0:
        return str(cur_dig)+str(only_evens(num // 10))
    #return only_evens(num // 10)
print("only even")
print(only_evens(1224))
#print(only_evens(0))

def is_power_of(base, num):
    ispower=False
    if (num == base):
        return True
    elif (num==0):
        return False
    else:

        for i in range(2,num/2):
            if base*base*i == num:
                ispower=True
                break
    return ispower



#print(is_power_of(7, 7))
#print(is_power_of(7, 0))


def cut(a_list):
    updlist = []
    indextoskip=-1;
    for index in range(len(a_list)):
        if index <=len(a_list):
            if a_list[index]<0:
                indextoskip=index+1
                continue
            elif (index==indextoskip):
                continue
            else:
                updlist.append(a_list[index])
    return updlist
#print(cut([7, 4, -2, 1, 9]))
#print(cut([-4, -7, -2, 1, 9]))
#print(cut([-3, -4, 5, -4, 1]))
print(cut([5, 7, -1, 6, -3, 1, 8, 785, 5, -2, 1, 0, 42]))
[5, 7, 6, 785, 5, 0, 42]

def cut_recur(a_list,updlist=None,indextoskip=-1):

    for index in range(len(a_list)):
        if index <=len(a_list):
            if a_list[index]<0:
                indextoskip=index+1
                continue
            elif (index==indextoskip):
                continue
            else:
                updlist.append(a_list[index])
    return updlist


# Recursive function - returns the number of negative numbers in a list
def CalcSumNegativeNumbers(A):
    if A == []:
        # if set is empty, return 0
        return 0
    else:
        # Calculate the count, go to further processing
        # without first item
        count = CalcSumNegativeNumbers(A[1:]) # recursive call of the same function

        # Increase by 1, provided that the current number is negative
        if A[0]<0:
            count = count + 1

        return count

# Demonstration of using the CalcSumNumbers() function
# 1. Create a set of numbers
L = [ -2, 3, 8, -11, -4, 6 ]

# 2. Call the function
n = CalcSumNegativeNumbers(L)

# 3. Print the sum
print("n = ", n)


def CutNegativeNumbers(A):
    if A == []:
        # if set is empty, return 0
        return []
    else:
        # Calculate the count, go to further processing
        # without first item


        updlist = CutNegativeNumbers(A[1:]) # recursive call of the same function

        # Increase by 1, provided that the current number is negative


        if A[0]>0:
            updlist.append(A[0])

        return updlist

# Demonstration of using the CalcSumNumbers() function
# 1. Create a set of numbers
L = [7, 4, -2, 1, 9]

# 2. Call the function
lst = CutNegativeNumbers(L)

# 3. Print the list
print("updlist = ", lst)


def CalcSumNumbers(A):
    summ = 0

    # here you need to implement a traversal in a loop
    for t in A:
        # The item t is processed
        if not isinstance(t, list): # check if t is a list
            summ = summ + t # if t is not a list, then add it to the sum
        else:
            # get sum from following recursive calls
            summ = summ + CalcSumNumbers(t)
    return summ
# Demonstration of using the CalcSumNumbers() function
# 1. Create a set of numbers
L = [-2, 3, 8, 11,[10,20]]

# 2. Call the function
summ = CalcSumNumbers(L)

# 3. Print the sum
print("summ = ", summ)


# Recursive function. Determine the maximum list item
def GetMaxList(L):
    if len(L)>1:
        # Get the most out of the following recursive calls
        Max = GetMaxList(L[1:])

        # Compare maximum with the first element of the list
        if L[0]<Max:
            return Max
        else:
            return L[0]

    if len(L)==1: # the last item in the list
        return L[0] # return this item

# Demonstration of using the Power() function
L = [ 500, 2300, 800, 114, 36]
res = GetMaxList(L)
print("res = ", res)


def cut(lst,ttl=[],previous=False):
    """
    if len(lst)==0:
        return 0
    """
    if lst==[]:
        return
    if(lst[0]>0):
        if(previous):
            pass
        else:
            ttl.append(lst[0])
        cut(lst[1:],ttl,False)
    else:
        cut(lst[1:],ttl,True)
    return ttl

ttl =cut([10,20,-30,-40,30,-40,50,60])
print("final")
print(ttl)


