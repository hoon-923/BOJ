# -*- coding: utf-8 -*-
"""[12864번] 평범한 배낭.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JZRWYmNIJB8cmg6aXNM__4de0nIVL1aE
"""

import sys
r = sys.stdin.readline
N,K = map(int,r().split())
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
bag =[[0,0] for _ in range(N+1)]
for i in range(1,N+1):
	W,V = map(int,r().split())
	bag[i][0] = W
	bag[i][1] = V

for i in range(1,N+1):
	for j in range(1,K+1):
		w,v = bag[i][0],bag[i][1]
		if j < w:
			dp[i][j] = dp[i-1][j]
		else:
			dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

print(dp[N][K])