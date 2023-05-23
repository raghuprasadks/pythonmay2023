"""
list - dynamic,heterogeneous,ordered,indexable,duplicate
"""
numbers=[29,45,'33',67,45]
print("numbers list ",numbers)
print("numbers list ",type(numbers))
print("length of numbers list ",len(numbers))
print("Element at 2 nd index ",numbers[2])
#print("Element at 6 th index ",numbers[6]) throws error
print("Element at -1 index ",numbers[-1])
print("append ")
numbers.append(99)
print("numbers list after append ",numbers)

print("loop ")
for num in numbers:
    print(num)
print("list constructor")
runs = list([23,24,27,31])
print("runs ",runs)

colors = []
colors.append("white")
colors.append("block")
colors.append("red")
print("colors ",colors)







