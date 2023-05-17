n=int(input())
l=list(map(int,input().split()))
j=[]
for i in l:
    if i==0:
        j.insert(0,i)
    else:
        j.append(i)
print(*j)