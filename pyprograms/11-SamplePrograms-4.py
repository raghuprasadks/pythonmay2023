"""
Fibonacci series

0 1 1 2 3 5
"""
"""
terms = int(input("enter the numbers of terms"))

fn = 0
sn = 1
print(fn,end=' ')
print(sn,end=' ')
terms = terms-2
while (terms >0):
    tn = fn +sn
    print(tn,end=' ')
    fn=sn
    sn =tn
    terms = terms-1

"""
def fibonacci(terms):
    fn = 0
    sn = 1
    print(fn, end=' ')
    print(sn, end=' ')
    terms = terms - 2
    while (terms > 0):
        tn = fn + sn
        print(tn, end=' ')
        fn = sn
        sn = tn
        terms = terms - 1

terms = int(input("enter the numbers of terms"))
fibonacci(terms)



"""
Without using list comprehension
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
"""
list comprehension
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

def hailstone(num):
    hailstone_list = []
    hailstone_list.append(num)
    while (num!=1) :
        if (num % 2 == 0):
            temp=num//2
            hailstone_list.append(temp)
            num=temp
        else :
            temp=3*num+1
            hailstone_list.append(temp)
            num=temp
    return hailstone_list
hail_list=hailstone(5)
print("Hailstone values :",hail_list)