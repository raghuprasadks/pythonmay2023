"""
Sample programs using user inputs
1. Print even numbers between given two number
Enter a first number -10
Enter last number - 20
10,12,...20
"""
print("Even numbers between two given numbers")

fn = int(input("Enter first number"))
sn = int(input("Enter second number"))
print("For loop")
for n in range(fn,sn+1,1):
    if(n%2==0):
        print(n)

print("while loop")

fn = int(input("Enter first number"))
sn = int(input("Enter second number"))

while (fn <=sn):
    if(fn%2==0):
        print(fn)
    fn=fn+1
print("using a function")

def evennumbers(fn,sn):
    for n in range(fn, sn + 1, 1):
        if (n % 2 == 0):
            print(n)
print("fn ",fn)
print("sn ",sn)
fn = int(input("Enter first number"))
sn = int(input("Enter second number"))

evennumbers(fn,sn)