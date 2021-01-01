# -*- coding: utf-8 -*-
"""[2606번] 바이러스.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JZRWYmNIJB8cmg6aXNM__4de0nIVL1aE
"""

import sys
r = sys.stdin.readline
N = int(r())
M = int(r())

edge = [[] for _ in range(N+1)]
for _ in range(M):
	A,B = map(int,r().split())
	edge[A].append(B)
	edge[B].append(A)

for e in edge:
	e.sort(reverse=True)

def virus():
	v = []
	stack = [1]
	visit = [False for _ in range(N+1)]
	while stack:
		node = stack.pop()
		if visit[node]:
			pass
		else:
			v.append(node)
			visit[node] = True
			stack += edge[node]
	return v

print(len(virus()) - 1)