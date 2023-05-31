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

print("print part of a list")
print(runs[2:4])
print("maximum ",max(runs))
print("minimum ",min(runs))
runs.sort()
print("sorted list ascending ",runs)
runs.reverse()
print("sorted list descending ",runs)



colors = []
colors.append("white")
colors.append("block")
colors.append("red")
print("colors ",colors)

ipltable=[]
header=["team","season","points"]
team1 = ["GT",2023,20]
team2 = ["CSK",2023,18]
ipltable.append(header)
ipltable.append(team1)
ipltable.append(team2)
print("ipl table ",ipltable)
totalpoints=0
for team in ipltable:
    print(team[0], " points : ",team[2])
    #totalpoints += team[2]

for index in range(len(ipltable)):
    if index ==0:
        continue
    team = ipltable[index]
    points = team[2]
    totalpoints = totalpoints+points
print("total points ",totalpoints)






