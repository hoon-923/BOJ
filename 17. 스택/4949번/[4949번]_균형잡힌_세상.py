import sys
r = sys.stdin.readline
while True:
	w = r().rstrip()
	if w == ".":
		break
	stack = []
	flag = 0
	for i in w:
		if i == "(" or i == "[":
			stack.append(i)
			
		elif i == ")":
			if len(stack) == 0 or stack[-1] == "[":
				flag = 1
				break
			else:
				stack.pop()
				
		elif i == "]":
			if len(stack) == 0 or stack[-1] == "(":
				flag = 1
				break
			else:
				stack.pop()
		
	if len(stack) == 0 and flag != 1:
		print("yes")
	else:
		print("no")
