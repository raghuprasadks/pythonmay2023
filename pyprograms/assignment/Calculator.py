#exp = "45+98-10"
#exp = '4        + 3 -       2' - passed
exp ='-2 +          3.5'
stack = []
i = 0
while i < len(exp):
	if exp[i].isdigit():
		num = int(exp[i])
		i += 1
		while i < len(exp) and exp[i].isdigit():
			num = num * 10 + int(exp[i])
			i += 1
		stack.append(num)
	elif exp[i] == "+":
		stack.append("+")
		i += 1
	elif exp[i] == "-":
		stack.append("-")
		i += 1
	else:
		i += 1

result = stack[0]
print("result ",result)
for i in range(1, len(stack), 2):
	if stack[i] == "+":
		result += stack[i+1]
	else:
		result -= stack[i+1]

print("The evaluated result is:", result)
