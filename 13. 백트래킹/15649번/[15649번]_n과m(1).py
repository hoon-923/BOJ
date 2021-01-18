# -*- coding: utf-8 -*-
"""[15649번] N과M(1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JZRWYmNIJB8cmg6aXNM__4de0nIVL1aE
"""

import sys
r=sys.stdin.readline
N,M = map(int, r().split())

num=[i+1 for i in range(N)]
check=[False]*N

res=[]

def dfs(cnt):
    if(cnt==M):
    	print(*res)
    	return
    
    for i in range(0, N):
        if(check[i]):
            continue

        check[i] = True
        res.append(num[i])
        dfs(cnt + 1)
        res.pop()
        check[i] = False
        
dfs(0)