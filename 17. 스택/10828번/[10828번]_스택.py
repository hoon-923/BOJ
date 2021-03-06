# -*- coding: utf-8 -*-
"""[10828번] 스택.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1loKqmSXACFkXo21AyG9Skn1TXWT8j8xY
"""

import sys
r = sys.stdin.readline
stack = []

def push(X):
	stack.append(X)

def pop():
	if len(stack) == 0:
		return -1
	else:
		return stack.pop()

def size():
	return len(stack)

def empty():
	if len(stack) == 0:
		return 1
	else:
		return 0

def top():
	if len(stack) == 0:
		return -1
	else:
		return stack[-1]

N = int(r())
for _ in range(N):
	s = r().rstrip()
	if s[:4] == "push":
		push(s[5:])
	elif s == "pop":
		print(pop())
	elif s == "size":
		print(size())
	elif s == "empty":
		print(empty())
	elif s == "top":
		print(top())