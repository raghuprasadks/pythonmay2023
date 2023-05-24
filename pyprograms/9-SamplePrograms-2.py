"""
1. Sum even number in a given list
numlist = [2,5,19,12,25,60]
"""
numlist = [2,5,19,12,25,60]
total = 0
for num in numlist:
    #print(num)
    if (num%2==0):
        total = total +num

print("total is ",total)

def evensum(numlist):
    total = 0
    for num in numlist:
        # print(num)
        if (num % 2 == 0):
            total = total + num
    return total

eventotal =evensum(numlist)
print("total of even numbers.. ",eventotal)
"""
2. list of list ipl players

"""

ipldashboard=[]
header = ["name","team","matches","runs","wickets"]
player1 = ["virat","rcb",14,500,0]
player2 = ["rohit","mi",14,350,0]
player3 = ["jadeja","csk",14,250,10]

ipldashboard.append(header)
ipldashboard.append(player1)
ipldashboard.append(player2)
ipldashboard.append(player3)

print("ipldashboard 2023")
print(ipldashboard)

print("all players")
for player in ipldashboard:
    print(player)

print("name and runs")
for player in ipldashboard:
    print(player[0],player[3])


print("total runs")
'''
totalruns=0
for player in ipldashboard:
    #totalruns = totalruns + player[2]

#print("total runs ",totalruns)
'''
totalruns = 0
totalwickets=0
for rowindex in range(len(ipldashboard)):
    if (rowindex==0):
        continue
    player = ipldashboard[rowindex]
    totalruns = totalruns + player[3]
    totalwickets = totalwickets + player[4]
print("total runs ",totalruns)
print("total wickets ",totalwickets)


'''    
for i in range(4):
    print(i)
'''


#print(ipldashboard[1])


"""
in  or not in
"""

marks = [20,24,11,39]

marktosearch=40
print(marktosearch in marks)

"""
Assignment ::
Question #4: joint_lst(lsts) 10 pts
Given a list of lists lsts, where each list contains numbers only, return a new list with all the 
numbers that appear in all the lists in lsts. You can assume that lsts contains at least one list.
Tip: You can check if an element is in a list with the in operator
Preconditions and Postconditions
lsts: list -> Integer smaller or greater than 1
Returns: list -> non-empty sequence of integers
Examples:
>>> joint_lst([[75.5, 1, 2, 3], [1, 3, 5], [0, 5, 9, 3, 1, -96, 8, 1]])
[1, 3]
>>> joint_lst([[1, 2, 3], [4, 5], [7, 8, 9, 10], [6, 89]])
[]

"""

lst = [[75.5, 1, 2, 3], [1, 3, 5], [0, 5, 9, 3, 1, -96, 8, 1]]
#lst =[[1, 2, 3], [4, 5], [7, 8, 9, 10], [6, 89]]
lst1 = lst[0]
lstnew = []
for searchelem in lst1:
    print(searchelem)
    isItemPresent=False
    for itemindex in range(len(lst)):
        item = lst[itemindex]
        if (itemindex == 0):
            continue;
        if (searchelem in item):
            isItemPresent = True
        if (isItemPresent):
            if (searchelem not in lstnew):
                lstnew.append(searchelem)

print("new list ",lstnew)

