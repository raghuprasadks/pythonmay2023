"""
Dictionary - key value pair
flower bracket
key should be unique
"""
aadhar = {123:'raghu',234:'ravi',123:'prasad'}
print(aadhar)
marks={'ravi':99,'rekha':58,'gaurav':78}
print(marks)
iplmatch={}
iplmatch['virat']=34
iplmatch['maxwel']=64
print('iplmatch ',iplmatch)
iplmatch['karthik']=18
print('iplmatch updated',iplmatch)
print("key value pair")
for k,v in iplmatch.items():
    print("key =",k)
    print("value =", v)

print ("keys only")
print(iplmatch.keys())

print ("vales only")
print(iplmatch.values())

search="virat"
for k,v in iplmatch.items():
    if(k==search):
        print(k,'exists')
        break
    else:
        print(k, 'does not exists')

name='virat kohli'
for n in name:
    print(n)
print("runs by virat  - get value using key",iplmatch["virat"])
print("change the value by using a key")
iplmatch['virat']=36
print("after update ",iplmatch)

print("length of dictionary ",len(iplmatch))
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print("thisdict ",thisdict)

print("data type of thisdict ",type(thisdict))

print("alternative way of creating a dictionary")
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
