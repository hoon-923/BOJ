import sys
r=sys.stdin.readline
N,M=map(int,r().split())
nums=[i+1 for i in range(N)]
res=[]

def dfs(cnt):
	if cnt==M:
		print(*res)
		return
	
	for i in range(N):
		res.append(nums[i])
		dfs(cnt+1)
		res.pop()

dfs(0)
