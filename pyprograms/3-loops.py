'''
Loops
while loop
for loop
indentation
'''
print("10's table in ascending order")
start = 10
end = 100
while (start <=end):
    print(start)
    start = start +10
print("out side the loop")

print("10's table in descending order")
start = 100
end = 10
while (start >=end):
    print(start)
    start = start -10
print("out side the loop")

print("0 to 9")
for num in range(10):
    print(num)
print("1 to 10")
for num in range(1,11):
    print(num)

print("10's table using for loop")
for num in range(10,100,10):
    print(num)

print("10's table using for loop in descending order")
for num in range(100,9,-10):
    print(num)

print("break")
for n in range(5,51,5):
    print(n)
    if(n == 25):
        break

print("continue")
for n in range(5,51,5):
    if(n == 25):
        continue
    print(n)



