n=int(input())
l=list(map(int,input().split()))
c=[]
z=0
for i in l:
    d=len(str(i))
    c.append(d)
f=min(c)
for j in c:
    if f==j:
        z+=1
print(z)