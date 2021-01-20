import sys
r=sys.stdin.readline
N,M=map(int,r().split())

nums=[i+1 for i in range(N)]
check=[False]*N
res=[]

def dfs(cnt):
	if cnt==M:
		print(*res)
		return
	
	for i in range(N):
		if check[i]:
			continue
		
		res.append(nums[i])
		dfs(cnt+1)
		res.pop()
		check[i]=True
		
		for j in range(i+1,N):
			check[j]=False

dfs(0)
