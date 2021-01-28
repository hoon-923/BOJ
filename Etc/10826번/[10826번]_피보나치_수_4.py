import sys
r=sys.stdin.readline
N=int(r())

def fibo_DP(n):
	a,b=0,1
	for i in range(n):
		a,b = b,a+b
	return a

print(fibo_DP(N))
