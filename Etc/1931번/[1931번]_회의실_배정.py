# -*- coding: utf-8 -*-
"""[1931번] 회의실 배정.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JZRWYmNIJB8cmg6aXNM__4de0nIVL1aE
"""

import sys
r=sys.stdin.readline
N=int(r())
l=[[0,0] for _ in range(N)]
res=[]
for i in range(N):
	start,end=map(int,r().split())
	l[i][0] = start
	l[i][1] = end
l.sort(key=lambda x:(x[1],x[0]))
res.append(l[0])
for i in range(1,N):
	if res[-1][1] <= l[i][0]:
		res.append(l[i])
print(len(res))