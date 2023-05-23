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
ipldashboard.append(header)
ipldashboard.append(player1)
ipldashboard.append(player2)
print("ipldashboard 2023")
print(ipldashboard)

print("all players")
for player in ipldashboard:
    print(player)

print("name and runs")
for player in ipldashboard:
    print(player[0],player[3])



