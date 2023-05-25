n=int(input())
l=list(map(int,input().split()))
k=0
c=[]
m=0
for i in l:
    k=len(str(i))
    c.append(k)
f=max(c)
for j in c:
    if j==f:
        m+=1
print(m)
    