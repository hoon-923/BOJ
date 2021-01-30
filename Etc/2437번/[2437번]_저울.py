import sys
r=sys.stdin.readline
N=int(r())
l=list(map(int,r().split()))
l.sort()

money=1
for i in l:
	if money < i:
		break
	money += i

print(money)
