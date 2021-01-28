from itertools import permutations
import sys
r=sys.stdin.readline
n,k=int(r()),int(r())
nums=[]
for _ in range(n):
	nums.append(r().rstrip())

res=[]
for i in permutations(nums,k):
	res.append(''.join(i))
res=set(res)
print(len(res))
