# -*- coding: utf-8 -*-
"""[2667번] 단지번호붙이기.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JZRWYmNIJB8cmg6aXNM__4de0nIVL1aE
"""

import sys
r = sys.stdin.readline
N = int(r())
map = []
for _ in range(N):
	map.append([int(i) for i in r().rstrip()])
check = [[True] * N for _ in range(N)]
danji = 0
q = []
apt = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
for y in range(N):
	for x in range(N):
		if map[y][x]:
			if check[y][x]:
				danji += 1
				cnt = 0
				q.append((x,y))
				while q:
					temp = q[0]
					q = q[1:]
					if check[temp[1]][temp[0]]:
						cnt += 1
						check[temp[1]][temp[0]] = False
						for i in range(4):
							new_x = temp[0] + dx[i]
							new_y = temp[1] + dy[i]
							if 0 <= new_x < N and 0 <= new_y < N and map[new_y][new_x] and check[new_y][new_x]:
								q.append((new_x,new_y))
				apt.append(cnt)
print(danji)
for i in sorted(apt):
	print(i)