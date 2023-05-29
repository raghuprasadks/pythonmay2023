"""
Pattern Generation
*
**
***
****
*****
"""
#print("welcome " *10)
r=int(input("Enter number of rows to print"))
#t=r
for num in range(1,r+1):
    print(" * " *num)

print("reverse")
for num in range(r,0,-1):
    print(" * " *num)
print("using while loop")
while (r>=1):
    print("*" *r)
    r=r-1




