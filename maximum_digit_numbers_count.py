n=int(input())
l=list(map(int,input().split()))
c=0
k=[]
v=[]
for i in l:
    c=len(str(i))
    k.append(c)
s=max(k)
for j in l:
    if len(str(j))==s:
        v.append(j)
print(*v)