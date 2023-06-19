"""
file management

w - write mode - creates a new file if the file does not
exists.Overwrites the file if a file exists
a - append mode
r - read mode
"""
print("create a file using write mode")
file = open("info.txt","w")
file.write("Sample File\n")
file.write("Writing sample text\n")
file.write("Writing another sample text\n")
file.close()

print("usage of append mode")
file = open("info.txt","a")
file.write("written using append mode\n")
file.write("written using append mode line 2\n")
file.close()

print("usage of read mode")
file = open("info.txt","r")
info =file.read()
print(info)
file.close()

print("usage of read mode - read line")
file = open("info.txt","r")
lines=file.readlines()
print("lines data type - ",type(lines))
for line in lines:
    print(line)


