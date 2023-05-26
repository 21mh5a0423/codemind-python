n=input()
x=n.split()
c=0
l=[]
for i in x:
    c=len(i)
    l.append(c)
print(max(l))