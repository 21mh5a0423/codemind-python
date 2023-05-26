s=input()
a=[]
l=0
k=s.split()
for i in k:
    l=i[::-1]
    a.append(l)
print(*a)