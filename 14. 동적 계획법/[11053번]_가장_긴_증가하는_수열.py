# -*- coding: utf-8 -*-
"""[11053번] 가장 긴 증가하는 수열.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1U3YL6pGmc3V0sq5tDlodosy-pC4iONqk
"""

import sys
r = sys.stdin.readline
N = int(r())
A = list(map(int,r().split()))
dp = []
dp.append(A[0])
for i in A:
  if i > dp[-1]:
    dp.append(i)
  else:
    for j in range(len(dp)):
    	if dp[j] >= i:
    		dp[j] = i
    		break
print(len(dp))