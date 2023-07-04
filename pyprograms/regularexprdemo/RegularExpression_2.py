import re
txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

x = re.findall("[a-m]", txt)
print(x)

txt = "That will be 599 dollars 786"

#Find all digit characters:

x = re.findall("\d", txt)
print(x)
