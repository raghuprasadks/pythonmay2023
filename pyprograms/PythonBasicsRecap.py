"""
Python Basics Recap
"""
print("Basic Data types - str,int,float,bool")
course  = 'Python'
duration = 6
hours = 30.0
isClassConducted = True
print("course ",course, " duration ",duration)
print(" course data type ",type(course))
print(" duration data type ",type(duration))
print(" hours data type ",type(hours))
print(f"Course : {course}")
print("Advanced data types - list,tuple,dictionary,set")
marks=[34,70,"twenty",90]
marks.append("56")
print("list after append ",marks)
print("slicing ",marks[1:4])
print("all elements",marks[::2])
print("all elements -1 : reverse",marks[::-1])
print("using negative index ",marks[-3])
#marks.sort()
#print("after sort ",marks)

runs=[20,33,12,25,13,16]
runs.sort()
print("runs in ascending order ",runs)
runs.reverse()
print("runs in descending order ",runs)
print("formating ")

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
print(f"I want .. {quantity} pieces of item {itemno} for {price} dollars")
print("tuple - constant list")
days = ("Mon","Tue","Wed","Thur","Fri")
print(days)
#days.append("sat")
print("set")
evenset={2,4,6,8,6,10}
print(evenset)

print("loops - while,for")
print("functions")

def add(num1,num2,num3=None):
    return num1+num2

res=add(100,133)
print("result ",res)






