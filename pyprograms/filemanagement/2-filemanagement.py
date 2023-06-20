file = open("sample.txt","r")

lines = file.readlines()
count = 0
for line in lines:
    words = line.split()
    #print(words)
    for word in words:
        print(word)
        count = count +1
        #pass
print("total number of words ",count)
file.close()