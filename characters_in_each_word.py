s=map(str,input().split())
c=0
l=[]
for i in s:
    for j in i:
        c=len(i)
    l.append(c)
print(*l)