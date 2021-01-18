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
