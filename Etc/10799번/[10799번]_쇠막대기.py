# -*- coding: utf-8 -*-
"""[10799번] 쇠막대기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JZRWYmNIJB8cmg6aXNM__4de0nIVL1aE
"""

import sys
r=sys.stdin.readline
metal=list(r().rstrip())
cnt=0
stack=[]
for i in range(len(metal)):
	if metal[i]=='(':
		stack.append(i)
	else:
		if metal[i-1]=='(':
			stack.pop()
			cnt+=len(stack)
		else:
			stack.pop()
			cnt+=1
print(cnt)