import sys
r=sys.stdin.readline

def BOJ_9184(a,b,c):
	
	if a<=0 or b<=0 or c<=0:
		return 1
	elif a>20 or b>20 or c>20:
		return BOJ_9184(20,20,20)
		
	if dp[a][b][c]:
		return dp[a][b][c]
		
	if a<b and b<c:
		dp[a][b][c] = BOJ_9184(a, b, c-1) + BOJ_9184(a, b-1, c-1) - BOJ_9184(a, b-1, c)
	else:
		dp[a][b][c] = BOJ_9184(a-1, b, c) + BOJ_9184(a-1, b-1, c) + BOJ_9184(a-1, b, c-1) - BOJ_9184(a-1, b-1, c-1)
	return dp[a][b][c]
	

dp = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while True:
	a,b,c=map(int,r().split())
	if a==-1 and b==-1 and c==-1:
		break
	print(f"w({a}, {b}, {c}) = {BOJ_9184(a,b,c)}")
