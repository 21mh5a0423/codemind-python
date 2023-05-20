import math
n=int(input())
aa=list(map(int,input().split()))
l=1
for i in aa:
    l=math.lcm(l,i)
print(l)
